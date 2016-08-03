import trafaret as t


twitterUrlsEntity = t.Dict({
    t.Key('url'): t.String,
    t.Key('expanded_url'): t.String,
    t.Key('display_url', optional=True): t.String,
    t.Key('indices'): t.List(t.Int)
})

twitterUserUrlsEntity = t.Dict({
    t.Key('url'): t.Dict({
        t.Key('urls'): t.List(twitterUrlsEntity)
    }),
    t.Key('description'): t.Dict({
        t.Key('urls'): t.List(twitterUrlsEntity) | t.Null
    })
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