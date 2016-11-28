synonyms = {
    'cheap': ['beanery', 'dump', 'inexpensive', 'competitive', 'economical', 'low cost',
              'low priced', 'low cost', 'low priced', 'at a bargain', 'bargain', 'budget', 'cheapo',
              'cost next to nothing', 'cut price', 'cut rate', 'easy on the pocket',
              'easy on packet', 'half priced', 'low tariff', 'marked down', 'popularly priced',
              'slashed', 'uncostly', 'affordable', 'cheapie',
              'cut rate', 'dime store', 'dirt cheap', 'el cheapo', 'low', 'low end',
              'reasonable', 'cheapish', 'discount', 'discounted', 'fire sale', 'lowered',
              'reduced', 'wholesale', 'supercheap', 'ultracheap', 'stingy', 'chintzy', 'closefisted', 'penny pinching',
              'sparingly priced', 'easy priced', 'low cost', 'soft priced'],
    'average': ['median', 'middling', 'midsize', 'midsized',
                'modest', 'conventional', 'normal',
                'usual', 'adequate', 'passable', 'tolerable', 'typical', 'mediocre',
                'moderate', 'moderately', 'regular', 'boilerplate', 'common',
                'fair', 'familiar', 'garden', 'general', 'humdrum', 'intermediate',
                'mainstream', 'medium', 'customary',
                'everyday', 'so so', 'undistinguished', 'unexceptional',
                'norm', 'par', 'standard', 'golden', 'mean', 'middle',
                'ordinary', 'status quo', 'exemplar', 'representative', 'considerable'],
    'expensive': ['high priced', 'costly', 'extravagant', 'fancy', 'high', 'lavish',
                  'overpriced', 'pricey', 'upscale', 'valuable', 'premium', 'big ticket',
                  'dear', 'excessive', 'exorbitant', 'holdup', 'immoderate', 'inordinate',
                  'invaluable', 'plush', 'posh', 'pretty', 'rich', 'ritzy',
                  'sky high', 'steep', 'swank', 'too high', 'uneconomical', 'star',
                  'unreasonable'],
    'near': ['close', 'nearby', 'closeby', 'convenient', 'within reach', 'at hand', 'around the corner',
             'not far', 'very near', 'at short distance away', 'neighboring', 'neighbouring', 'near at hand',
             'next door', 'close proximity', 'short'],
    'far': ['distant', 'remote', 'far flung', 'outlaying', 'on outlier', 'far off', 'a long way', 'at miles', 'afar',
            'off', 'away', 'extreme door'],
    'distance': ['area', 'gap', 'length', 'orbit', 'radius', 'size', 'space ', 'span ', 'width ', 'bit', 'breadth',
                 'extension', 'extent', 'farness', 'horizon', 'outskirts', 'provinces', 'reach', 'remoteness', 'spread',
                 'way', 'country', 'location', 'vicinity', 'located', 'proximity'],
    'yes': ['yeah', 'yea', 'ya', 'yup', 'affirmative', 'good', 'fine', 'ok', 'okay', 'kay', 'true', 'all right', 'aye',
            'roger that', 'certainly', 'definitely', 'exactly', 'positive', 'positively', 'precise', 'precisely',
            'of course', 'sure', 'undoubtedly'],
    'no': ['nope']
}
price_keywords = ['cheap', 'average', 'expensive']
cuisine_keywords = ['indian', 'italian', 'korean', 'chinese', 'mexican']
distance_keywords = ['near', 'far', 'average']

# NLG templates
request_price = "Are you looking for a cheap, average or expensive restaurant?"
request_cuisine = "What cuisine would you prefer?"
request_distance = "Are you looking for a restaurant which is near, far or at an average distance?"

confirm = "So, would you like {} {} restaurant which is {}?"

confirm_price = "So, would you like restaurant which is {}?"
confirm_distance = "So, would you like a restaurant which is {}"
confirm_cuisine = "So, would you like restaurant which serves {} food?"

response_no_restaurants = "Sorry. We could not find any restaurants that match your preferences."
response_restaurant_count = "I found {} that match your query."
response_restaurant_name_single = "The only available restaurant is {} located at {}."
response_restaurant_names = "The best ones as per service ratings are {} located at {} and {} located at {}."
# However, we found 5 (chinese) restaurants (that are cheap)
response_tradeoff_no_restaurant = "However, we found {} {} restaurants {}"
# However, we also found 5 more (chinese) restaurants (that are cheap)
response_tradeoff = "we also found {} more {} restaurants {}"