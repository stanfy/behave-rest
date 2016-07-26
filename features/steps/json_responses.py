import trafaret as t

"""
Example of using Trafaret (https://github.com/Deepwalker/trafaret) to describe json response structure

Assuming our json is:

{
   "access_token":"access_token",
   "refresh_token":"refresh_token",
   "token_type":"token_type",
   "expires_in":1800
}

Our trafaret will be:

tokenData = t.Dict({
    t.Key('access_token'): t.String,
    t.Key('refresh_token'): t.String,
    t.Key('token_type'): t.String,
    t.Key('expires_in'): t.Int
})
"""

# Below are objects used for validating response in test.feature
geoData = t.Dict({
    t.Key('lat'): t.String,
    t.Key('lng'): t.String
})

addressData = t.Dict({
    t.Key('street'): t.String,
    t.Key('suite'): t.String,
    t.Key('city'): t.String,
    t.Key('zipcode'): t.String,
    t.Key('geo'): geoData
})

companyData = t.Dict({
    t.Key('name'): t.String,
    t.Key('catchPhrase'): t.String,
    t.Key('bs'): t.String
})

usersData = t.List(
    t.Dict({
        t.Key('id'): t.Int,
        t.Key('name'): t.String,
        t.Key('username'): t.String,
        t.Key('email'): t.String,
        t.Key('address'): addressData,
        t.Key('phone'): t.String,
        t.Key('website'): t.String,
        t.Key('company'): companyData
    })
)

# Twitter search response jSON

twitterStatusMetaData = t.Dict({
    t.Key('iso_language_code'): t.String,
    t.Key('result_type'): t.String
})

twitterHashtagEntity = t.Dict({
    t.Key('text'): t.String,
    t.Key('indices'): t.List(t.Int)
})

twitterSymbolsEntity = t.Dict({

})

twitterUserMentionsEntity = t.Dict({
    t.Key('screen_name'): t.String,
    t.Key('name'): t.String,
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('indices'): t.List(t.Int)
})

twitterUrlsEntity = t.Dict({
    t.Key('url'): t.String,
    t.Key('expanded_url'): t.String,
    t.Key('display_url'): t.String,
    t.Key('indices'): t.List(t.Int)
})

twitterPhotoSizeData = t.Dict({
    t.Key('w'): t.Int,
    t.Key('h'): t.Int,
    t.Key('resize'): t.String
})

twitterMediaEntity = t.Dict({
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('indices'): t.List(t.Int),
    t.Key('media_url'): t.String,
    t.Key('media_url_https'): t.String,
    t.Key('url'): t.String,
    t.Key('display_url'): t.String,
    t.Key('expanded_url'): t.String,
    t.Key('type'): t.String,
    t.Key('sizes'): t.Dict({
        t.Key('small'): twitterPhotoSizeData,
        t.Key('thumb'): twitterPhotoSizeData,
        t.Key('large'): twitterPhotoSizeData,
        t.Key('medium'): twitterPhotoSizeData
    }),
    t.Key('source_status_id', optional=True): t.Int,
    t.Key('source_status_id_str', optional=True): t.String,
    t.Key('source_user_id', optional=True): t.Int,
    t.Key('source_user_id_str', optional=True): t.String
})

twitterStatusEntitiesData = t.Dict({
    t.Key('hashtags'): t.List(twitterHashtagEntity),
    t.Key('symbols'): t.List(twitterSymbolsEntity),
    t.Key('user_mentions'): t.List(twitterUserMentionsEntity),
    t.Key('urls'): t.List(twitterUrlsEntity) | t.Null,
    t.Key('media', optional=True): t.List(twitterMediaEntity) | t.Null
})

twitterCoordinatesEntity = t.List(t.List(t.Float))

twitterPlaceEntity = t.Dict({
    t.Key('id'): t.String,
    t.Key('url'): t.String | t.Null,
    t.Key('place_type'): t.String,
    t.Key('name'): t.String,
    t.Key('full_name'): t.String,
    t.Key('country_code'): t.String,
    t.Key('country'): t.String,
    t.Key('contained_within'): t.List(t.Dict({})),
    t.Key('bounding_box'): t.Dict({
        t.Key('type'): t.String,
        t.Key('coordinates'): t.List(twitterCoordinatesEntity) | t.Null
    }),
    t.Key('attributes', optional=True): t.Dict({
        t.Key('street_address'): t.String,
        t.Key('locality'): t.String,
        t.Key('region'): t.String,
        t.Key('iso3'): t.String,
        t.Key('postal_code'): t.String,
        t.Key('phone'): t.String,
        t.Key('twitter'): t.String,
        t.Key('url'): t.String,
        t.Key('id'): t.String
    }) | t.Dict({})
})

twitterUserUrlsEntity = t.Dict({
    t.Key('url'): t.Dict({
        t.Key('urls'): t.List(twitterUrlsEntity)
    }),
    t.Key('description'): t.Dict({
        t.Key('urls'): t.List(twitterUrlsEntity) | t.Null
    })
})

twitterContributorsData = t.Dict({
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('screen_name'): t.String,
})

twitterUserData = t.Dict({
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('name'): t.String,
    t.Key('screen_name'): t.String,
    t.Key('location'): t.String(allow_blank=True) | t.Null,
    t.Key('description'): t.String(allow_blank=True) | t.Null,
    t.Key('url', optional=True): t.String | t.Null,
    t.Key('entities'): t.Dict({
        t.Key('description'): t.Dict({
                t.Key('urls'): t.List(twitterUrlsEntity) | t.Null
            })
        }) | twitterUserUrlsEntity,
    t.Key('protected'): t.Bool,
    t.Key('followers_count'): t.Int,
    t.Key('friends_count'): t.Int,
    t.Key('listed_count'): t.Int,
    t.Key('created_at'): t.String,
    t.Key('favourites_count'): t.Int,
    t.Key('utc_offset'): t.Int | t.Null,
    t.Key('time_zone'): t.String | t.Null,
    t.Key('geo_enabled'): t.Bool,
    t.Key('verified'): t.Bool,
    t.Key('statuses_count'): t.Int,
    t.Key('lang'): t.String,
    t.Key('contributors_enabled'): t.Bool,
    t.Key('is_translator'): t.Bool,
    t.Key('is_translation_enabled'): t.Bool,
    t.Key('profile_background_color'): t.String,
    t.Key('profile_background_image_url', optional=True): t.String | t.Null,
    t.Key('profile_background_image_url_https'): t.String | t.Null,
    t.Key('profile_background_tile'): t.Bool,
    t.Key('profile_image_url'): t.String,
    t.Key('profile_image_url_https'): t.String,
    t.Key('profile_link_color'): t.String,
    t.Key('profile_sidebar_border_color'): t.String,
    t.Key('profile_sidebar_fill_color'): t.String,
    t.Key('profile_text_color'): t.String,
    t.Key('profile_use_background_image'): t.Bool,
    t.Key('has_extended_profile'): t.Bool,
    t.Key('default_profile'): t.Bool,
    t.Key('default_profile_image'): t.Bool,
    t.Key('following'): t.Null,
    t.Key('follow_request_sent'): t.Null,
    t.Key('notifications'): t.Null,
    t.Key('profile_banner_url', optional=True): t.String
})

twitterRetweetedStatusData = t.Dict({
    t.Key('created_at'): t.String,
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('text'): t.String,
    t.Key('truncated'): t.Bool,
    t.Key('entities'): twitterStatusEntitiesData | t.Null,
    t.Key('metadata'): twitterStatusMetaData | t.Null,
    t.Key('source'): t.String,
    t.Key('in_reply_to_status_id'): t.Int | t.Null,
    t.Key('in_reply_to_status_id_str'): t.String | t.Null,
    t.Key('in_reply_to_user_id'): t.Int | t.Null,
    t.Key('in_reply_to_user_id_str'): t.String | t.Null,
    t.Key('in_reply_to_screen_name'): t.String | t.Null,
    t.Key('user'): twitterUserData,
    t.Key('geo'): geoData | t.Null,
    t.Key('coordinates'): twitterCoordinatesEntity | t.Null,
    t.Key('place'): twitterPlaceEntity | t.Null,
    t.Key('contributors'): t.List(twitterContributorsData) | t.Null,
    t.Key('is_quote_status'): t.Bool,
    t.Key('retweet_count'): t.Int,
    t.Key('favorite_count'): t.Int,
    t.Key('favorited'): t.Bool,
    t.Key('retweeted'): t.Bool,
    t.Key('lang'): t.String,
    t.Key('quoted_status_id', optional=True): t.Int | t.Null,
    t.Key('quoted_status_id_str', optional=True): t.String | t.Null,
    t.Key('possibly_sensitive', optional=True): t.Bool
})

twitterStatusData = t.Dict({
    t.Key('created_at'): t.String,
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('text'): t.String,
    t.Key('metadata'): twitterStatusMetaData | t.Null,
    t.Key('truncated'): t.Bool,
    t.Key('entities'): twitterStatusEntitiesData | t.Null,
    t.Key('user'): twitterUserData,
    t.Key('source'): t.String,
    t.Key('in_reply_to_status_id'): t.Int | t.Null,
    t.Key('in_reply_to_status_id_str'): t.String | t.Null,
    t.Key('in_reply_to_user_id'): t.Int | t.Null,
    t.Key('in_reply_to_user_id_str'): t.String | t.Null,
    t.Key('in_reply_to_screen_name'): t.String | t.Null,
    t.Key('geo'): geoData | t.Null,
    t.Key('coordinates'): twitterCoordinatesEntity | t.Null,
    t.Key('place'): twitterPlaceEntity | t.Null,
    t.Key('contributors'): t.List(twitterContributorsData) | t.Null,
    t.Key('retweeted_status', optional=True): twitterRetweetedStatusData | t.Null,
    t.Key('is_quote_status'): t.Bool,
    t.Key('retweet_count'): t.Int,
    t.Key('favorite_count'): t.Int,
    t.Key('favorited'): t.Bool,
    t.Key('retweeted'): t.Bool,
    t.Key('lang'): t.String,
    t.Key('possibly_sensitive', optional=True): t.Bool,
    t.Key('quoted_status_id', optional=True): t.Int | t.Null,
    t.Key('quoted_status_id_str', optional=True): t.String | t.Null,
    t.Key('quoted_status', optional=True): twitterRetweetedStatusData | t.Null
})

twitterSearchMetaData = t.Dict({
    t.Key('completed_in'): t.Float,
    t.Key('max_id'): t.Int,
    t.Key('max_id_str'): t.String,
    t.Key('next_results', optional=True): t.String,
    t.Key('query'): t.String,
    t.Key('refresh_url'): t.String,
    t.Key('count'): t.Int,
    t.Key('since_id'): t.Int,
    t.Key('since_id_str'): t.String
})

twitterSearchData = t.Dict({
    t.Key('statuses'): t.List(twitterStatusData),
    t.Key('search_metadata'): twitterSearchMetaData
})

# Twitter timeline response jSON

twitterTimelineRetweetData = t.Dict({
    t.Key('created_at'): t.String,
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('text'): t.String,
    t.Key('truncated'): t.Bool,
    t.Key('entities'): twitterStatusEntitiesData | t.Null,
    t.Key('source'): t.String,
    t.Key('in_reply_to_status_id'): t.Int | t.Null,
    t.Key('in_reply_to_status_id_str'): t.String | t.Null,
    t.Key('in_reply_to_user_id'): t.Int | t.Null,
    t.Key('in_reply_to_user_id_str'): t.String | t.Null,
    t.Key('in_reply_to_screen_name'): t.String | t.Null,
    t.Key('user'): twitterUserData,
    t.Key('geo'): geoData | t.Null,
    t.Key('coordinates'): twitterCoordinatesEntity | t.Null,
    t.Key('place'): twitterPlaceEntity | t.Null,
    t.Key('contributors'): t.List(twitterContributorsData) | t.Null,
    t.Key('is_quote_status'): t.Bool,
    t.Key('retweet_count'): t.Int,
    t.Key('favorite_count'): t.Int,
    t.Key('favorited'): t.Bool,
    t.Key('retweeted'): t.Bool,
    t.Key('lang'): t.String,
    t.Key('quoted_status_id', optional=True): t.Int | t.Null,
    t.Key('quoted_status_id_str', optional=True): t.String | t.Null,
    t.Key('possibly_sensitive', optional=True): t.Bool
})

twitterUserTimelineData = t.List(t.Dict({
    t.Key('created_at'): t.String,
    t.Key('id'): t.Int,
    t.Key('id_str'): t.String,
    t.Key('text'): t.String,
    t.Key('truncated'): t.Bool,
    t.Key('entities'): twitterStatusEntitiesData | t.Null,
    t.Key('user'): twitterUserData,
    t.Key('source'): t.String,
    t.Key('in_reply_to_status_id'): t.Int | t.Null,
    t.Key('in_reply_to_status_id_str'): t.String | t.Null,
    t.Key('in_reply_to_user_id'): t.Int | t.Null,
    t.Key('in_reply_to_user_id_str'): t.String | t.Null,
    t.Key('in_reply_to_screen_name'): t.String | t.Null,
    t.Key('geo'): geoData | t.Null,
    t.Key('coordinates'): twitterCoordinatesEntity | t.Null,
    t.Key('place'): twitterPlaceEntity | t.Null,
    t.Key('contributors'): t.List(twitterContributorsData) | t.Null,
    t.Key('retweeted_status', optional=True): twitterTimelineRetweetData | t.Null,
    t.Key('is_quote_status'): t.Bool,
    t.Key('retweet_count'): t.Int,
    t.Key('favorite_count'): t.Int,
    t.Key('favorited'): t.Bool,
    t.Key('retweeted'): t.Bool,
    t.Key('lang'): t.String,
    t.Key('possibly_sensitive', optional=True): t.Bool,
    t.Key('quoted_status_id', optional=True): t.Int | t.Null,
    t.Key('quoted_status_id_str', optional=True): t.String | t.Null,
    t.Key('quoted_status', optional=True): twitterTimelineRetweetData | t.Null,
}))
