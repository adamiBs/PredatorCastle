module.exports = {
    calculateSuspition: function (profile) {
        var EMPTY_FIELD = 'Empty Field'
        var statisticsJSON = {
            tab_friends: {
                name: "friends",
                fields: {
                    number_of_friends: {
                        name: "Number of friends",
                        fields: {
                            number_of_males: {
                                name: "Number of male friends",
                                value: profile.friendData.gender.males === 0 ? EMPTY_FIELD : profile.friendData.gender.males.toString()
                            }, 
                            number_of_males: {
                                name: "Number of female friends",
                                value: profile.friendData.gender.females === 0 ? EMPTY_FIELD : profile.friendData.gender.females.toString()
                            }, 
                            number_of_unknown: {
                                name: "Number of unknown gender friends",
                                value: profile.friendData.gender.unknown === 0 ? EMPTY_FIELD : profile.friendData.gender.unknown.toString()
                            }, 
                            total: {
                                name: "Total number of friends",
                                value: profile.friendData.amount === 0 ? EMPTY_FIELD : profile.friendData.amount.toString()
                            }
                        }
                    },
                    common_values: {
                        name: "Common values with friends",
                        fields: {
                            number_same_work: {
                                name: "Number of friends with same work", 
                                value: profile.friendData.common.work === 0 ? EMPTY_FIELD : profile.friendData.common.work.toString()
                            },
                            number_same_city: {
                                name: "Number of friends with same home city", 
                                value: profile.friendData.common.city === 0 ? EMPTY_FIELD : profile.friendData.common.city.toString()
                            },
                            number_same_study: {
                                name: "Number of friends with same study", 
                                value: profile.friendData.common.study === 0 ? EMPTY_FIELD : profile.friendData.common.study.toString()
                            }
                        }
                    }
                }
            },
            tab_profile: {
                name: "profile",
                fields: {
                    LiveIn: {
                        name: "Lives in",
                        value: profile.personalData.city === 0 ? EMPTY_FIELD : profile.personalData.city.toString()
                    },
                    WorkPlace: {
                        name: "Works at",
                        value: profile.personalData.work === 0 ? EMPTY_FIELD : profile.personalData.work.toString()
                    },
                    StudyPlace: {
                        name: "Studies at",
                        value: profile.personalData.study === 0 ? EMPTY_FIELD : profile.personalData.study.toString()
                    }
                }
            }
        };
        return (statisticsJSON);
    }
};
