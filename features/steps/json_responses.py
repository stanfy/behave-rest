import trafaret as t

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
