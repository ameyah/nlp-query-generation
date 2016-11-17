import json
import unicodedata
import re

__author__ = 'Ameya'


class Controllers():
    def __init__(self):
        self.participantObj = participant.Participant()

    @staticmethod
    def clear_plain_text_data():
        post_queries.clear_plain_text_data()

    def new_participant_record(self, one_way_hash):
        participant_id = get_queries.get_participant_id(one_way_hash)
        self.participantObj.set_participant_id(participant_id)
        return participant_id

    def get_study_questions(self, questions_type):
        if questions_type == "CURRENT" or questions_type == "RISK" or questions_type == "POST":
            questions = get_queries.get_study_questions(questions_type)
            questions = [{"question_id": int(elem['question_id']),
                          "question": unicodedata.normalize('NFKD', unicode(elem['question'], errors='ignore'))} for
                         elem in questions]
            if len(questions) > 0:
                if questions_type == "POST":
                    websites = get_queries.get_participant_logged_websites(self.participantObj.get_participant_id())
                    result_obj = {
                        "questions": questions,
                        "websites": []
                    }
                    for website in websites:
                        website_obj = {
                            "id": website['website_id'],
                            "text": website['website_text']
                        }
                        result_obj['websites'].append(website_obj)
                    return result_obj
                return questions

    def transform_credentials(self, website_info_dict):
        # For websiteUrl, first check whether participantObj has an active url
        active_website = self.participantObj.get_active_website()
        if active_website != '':
            website_url = active_website
        else:
            website_url = website_info_dict['active_url']
            previous_active_website = self.participantObj.get_previous_active_website()
            if utils.check_website_syntactic_similarity(website_url, previous_active_website):
                website_url = previous_active_website

        clear_password_uri_decoded = utils.url_decode(website_info_dict['clear_password'])
        try:
            clear_username_uri_decoded = utils.url_decode(website_info_dict['clear_username'])
        except AttributeError:
            clear_username_uri_decoded = self.participantObj.get_previous_username()
        except KeyError:
            clear_username_uri_decoded = self.participantObj.get_previous_username()

        print website_info_dict['active_url']
        if website_info_dict['active_url'] == "undefined":
            website_info_dict['active_url'] = self.participantObj.get_previous_url()

        # First insert the login website in the database
        transformed_cred_id = get_queries.get_transformed_credentials_id(self.participantObj.get_participant_id(),
                                                                         website_url,
                                                                         website_info_dict['password_strength'],
                                                                         website_info_dict['password_warning'])
        self.participantObj.set_transformed_cred_id(transformed_cred_id)

        # store length and uppercase info for clear text password
        password_length = len(website_info_dict['clear_password'])
        password_all_uppercase = utils.escape(website_info_dict['clear_password']).isupper()
        post_queries.store_password_length_uppercase_info(transformed_cred_id, password_length, password_all_uppercase)

        segmentation.segment_word(clear_password_uri_decoded, True, self.participantObj.get_participant_id())
        pos_tag.pos_tag_word(self.participantObj.get_participant_id())
        generate_grammar.generate_grammar(self.participantObj.get_participant_id(), transformed_cred_id,
                                          clear_password=clear_password_uri_decoded)

        # Delete original password after transformation
        self.clear_plain_text_data()

        # Transform usernames semantically. We'll use the same functions for now.
        # as the procedure is same, except that we dont have to store grammar.
        # First check if username is email, if it is then extract email username and transform only the
        # username
        email_split_flag = False
        if re.match("[^@]+@[^@]+\.[^@]+", clear_username_uri_decoded):
            email_username = clear_username_uri_decoded.split("@")[0]
            email_split_flag = True
        else:
            email_username = clear_username_uri_decoded
        segmentation.segment_word(email_username, False, self.participantObj.get_participant_id())
        pos_tag.pos_tag_word(self.participantObj.get_participant_id())
        generate_grammar.generate_grammar(self.participantObj.get_participant_id(), transformed_cred_id,
                                          type="username")

        if email_split_flag:
            # Now append the email domain to the transformed Username
            email_domain = "@" + clear_username_uri_decoded.split("@")[1]
            post_queries.append_email_domain_username(transformed_cred_id, email_domain)

        # store clearUsername and active url in participantObj
        self.participantObj.set_active_username(clear_username_uri_decoded)
        self.participantObj.set_active_url(website_info_dict['active_url'])
        self.clear_plain_text_data()

        self.participantObj.inc_website_count()
        print "Websites done: " + str(self.participantObj.get_website_count())

        self.participantObj.reset_active_website()

    def get_participant_results(self, one_way_hash):
        # First clear the password hashes
        post_queries.clear_password_key()
        words_mapping.clear_word_mapping()
        result_dict = get_queries.get_transformed_passwords_results(one_way_hash)
        return result_dict

    def get_website_importance(self, website_url):
        importance = None
        if website_url != '':
            probability = get_queries.get_website_probability(website_url)
            importance = utils.check_website_importance(probability)
        return importance

    def get_website_list_probability(self, website_list):
        website_list_info = []
        website_list = json.loads(website_list)
        for website in website_list:
            url = website['url']
            importance = self.get_website_importance(url)
            if importance is not None:
                website_info = {
                    'id': website['id'],
                    'url': url,
                    'important': importance
                }
                website_list_info.append(website_info)
        return website_list_info

    def save_auth_status(self, auth_status):
        transformed_cred_id = self.participantObj.get_transformed_cred_id()
        post_queries.save_auth_status(transformed_cred_id, int(auth_status))

    def insert_prestudy_answers(self, postvars):
        answers = json.loads(postvars['answers'][0])
        result = post_queries.insert_prestudy_answers(self.participantObj.get_participant_id(), answers)
        return result

    def insert_poststudy_answers(self, postvars):
        answers = json.loads(postvars['answers'][0])
        result = post_queries.insert_poststudy_answers(self.participantObj.get_participant_id(), answers)
        return result

    def save_user_website_list(self, postvars):
        website_list_data = json.loads(postvars['data'][0])
        # save website list
        post_queries.insert_website_list(self.participantObj.get_participant_id(), website_list_data)

    def set_participant_id(self, postvars):
        # Clear password hashes just to make sure we are clear
        post_queries.clear_password_key()
        words_mapping.clear_word_mapping()
        self.participantObj.set_participant_id(int(postvars['id'][0]))

    def add_new_user_website(self, postvars):
        website_url = str(postvars['url'][0])
        website_importance = int(postvars['importance'][0])
        website_frequency = int(postvars['frequency'][0])
        result = post_queries.add_new_website(self.participantObj.get_participant_id(), website_url, website_importance,
            website_frequency)
        return result

    def set_active_website(self, postvars):
        self.participantObj.set_active_website(str(postvars['url'][0]))