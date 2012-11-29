class BoardType:
    ADS = 0
    CM = 1
    CP = 2
    OPS = 3
    GEN = 4

class EventType:
    NONE = -1
    ASSIST = 0
    PROJECT = 1
    TRAINING = 2
    SEMINAR = 3
    MEETING = 4

class EventStatus:
    DENIED = -1
    REQUESTED = 0
    APPROVED = 1

reqs = [#ads
        {'name': 'Ads Assist',
         'quantity': 3,
         'board': BoardType.ADS,
         'event': EventType.ASSIST,
         'notes': ""},
        {'name': 'Ads Department Meeting',
         'quantity': 1,
         'board': BoardType.ADS,
         'event': EventType.MEETING,
         'notes': ""},
        {'name': 'Tearsheet',
         'quantity': 6,
         'board': BoardType.ADS,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Stuffing',
         'quantity': 2,
         'board': BoardType.ADS,
         'event': EventType.NONE,
         'notes': ""},
        
        #cm
        {'name': 'C&M Assist',
         'quantity': 3,
         'board': BoardType.CM,
         'event': EventType.ASSIST,
         'notes': ""},
        {'name': 'C&M Department Meeting',
         'quantity': 1,
         'board': BoardType.CM,
         'event': EventType.MEETING,
         'notes': ""},
        {'name': 'Marketing Project',
         'quantity': 1,
         'board': BoardType.CM,
         'event': EventType.PROJECT,
         'notes': ""},
        {'name': 'Resubscription',
         'quantity': 3,
         'board': BoardType.CM,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Free Trial Subscription',
         'quantity': 5,
         'board': BoardType.CM,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Subscription',
         'quantity': 3,
         'board': BoardType.CM,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Audit Session',
         'quantity': 2,
         'board': BoardType.CM,
         'event': EventType.NONE,
         'notes': ""},

        
        #cp
        {'name': 'CP Assist',
         'quantity': 2,
         'board': BoardType.CP,
         'event': EventType.ASSIST,
         'notes': ""},
        {'name': 'CP Department Meeting',
         'quantity': 1,
         'board': BoardType.CP,
         'event': EventType.MEETING,
         'notes': ""},
        {'name': 'CP Project',
         'quantity': 1,
         'board': BoardType.CP,
         'event': EventType.PROJECT,
         'notes': ""},
        {'name': 'Production Job',
         'quantity': 2,
         'board': BoardType.CP,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Press Run',
         'quantity': 1,
         'board': BoardType.CP,
         'event': EventType.NONE,
         'notes': ""},
        {'name': 'Shadowing',
         'quantity': 1,
         'board': BoardType.CP,
         'event': EventType.NONE,
         'notes': ""},

        #ops
        {'name': 'Ops Assist',
         'quantity': 2,
         'board': BoardType.OPS,
         'event': EventType.ASSIST,
         'notes': ""},
        {'name': 'Ops Department Meeting',
         'quantity': 1,
         'board': BoardType.OPS,
         'event': EventType.MEETING,
         'notes': ""},
        {'name': 'Data Analysis Project',
         'quantity': 1,
         'board': BoardType.OPS,
         'event': EventType.PROJECT,
         'notes': ""},

        #gen
        {'name': 'General Assist',
         'quantity': 3,
         'board': BoardType.GEN,
         'event': EventType.ASSIST,
         'notes': ""},
        {'name': 'Phone Training',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.TRAINING,
         'notes': ""},
        {'name': 'Ads Training',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.TRAINING,
         'notes': ""},
        {'name': 'Personalized Pitch Training',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.TRAINING,
         'notes': ""},
        {'name': 'Circulation Database/Archive Training',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.TRAINING,
         'notes': ""},
        {'name': 'CP Solicitation Training',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.TRAINING,
         'notes': ""},
        
        #seminars
        {'name': 'Business Crisis Seminar',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.SEMINAR,
         'notes': ""},
        {'name': 'Pitch Seminar',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.SEMINAR,
         'notes': ""},
        {'name': 'Libel Seminar',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.SEMINAR,
         'notes': ""},
        {'name': 'Crimson History Seminar',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.SEMINAR,
         'notes': ""},
        
        #biz meals
        {'name': 'Biz Meal',
         'quantity': 4,
         'board': BoardType.GEN,
         'event': EventType.MEETING,
         'notes': ""},
        
        #midpoint and final stuff
        {'name': 'Midpoint Project',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.PROJECT,
         'notes': ""},
        {'name': 'Final Project',
         'quantity': 1,
         'board': BoardType.GEN,
         'event': EventType.PROJECT,
         'notes': ""}
        ]
