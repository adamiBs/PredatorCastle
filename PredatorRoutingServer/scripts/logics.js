module.exports = {
    calculateSuspition: function (profile) {
        var statisticsJSON = {
            tab_friends: {
                name: "friends",
                value: {
                    number_of_friends: {
                        name: "Number of friends",
                        value: {
                            number_of_males: {
                                name: "Number of male friends",
                                value: profile.friendData.gender.males
                            }, 
                            number_of_males: {
                                name: "Number of female friends",
                                value: profile.friendData.gender.females
                            }, 
                            number_of_unknown: {
                                name: "Number of unknown friends",
                                value: profile.friendData.gender.unknown
                            }, 
                            total: {
                                name: "Total number of friends",
                                value: profile.friendData.amount
                            }
                        }
                    },
                    common_values: {
                        name: "Common values with friends",
                        value: {
                            number_same_work: {
                                name: "Number of friends with same work", 
                                value: profile.friendData.common.work
                            },
                            number_same_city: {
                                name: "Number of friends with same home city", 
                                value: profile.friendData.common.city
                            },
                            number_same_study: {
                                name: "Number of friends with same study", 
                                value: profile.friendData.common.study
                            }
                        }
                    }
                }
            },
            tab_profile: {
                name: "profile",
                value: {
                    age: {
                        name: "Age",
                        value: "19"
                    },
                    LiveIn: {
                        name: "Live In",
                        value: "Kadima"
                    },
                    WorkPlace: {
                        name: "Work Place",
                        value: "Facebook"
                    }
                }
            }
        };
        return (profile);
    }
};
