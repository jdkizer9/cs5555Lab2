from rauth import OAuth2Service
import base64
from django.http import HttpResponseRedirect
import json

class DPUNetworkController(object):

    __instance_map = {}

    @classmethod
    def RegisterClient(cls, name, instance):
        cls.__instance_map[name] = instance
        print cls.__instance_map

    @classmethod
    def CheckForClient(cls, name):
        return name in cls.__instance_map

    @classmethod
    def GetClient(cls, name):
        print cls.__instance_map
        return cls.__instance_map[name]

    def __init__(self, name, client_id, client_secret):
        self.name = name
        self.service_name = 'omh-client-' + name
        self.client_id = client_id
        self.client_secret = client_secret
        self.service = OAuth2Service(
            name=self.service_name,
            client_id=self.client_id,
            client_secret=self.client_id,
            access_token_url='https://ohmage-omh.smalldata.io/dsu/oauth/token',
            authorize_url='https://ohmage-omh.smalldata.io/dsu/oauth/authorize',
            base_url='https://ohmage-omh.smalldata.io/dsu/')
        self.session = None
        self.access_token = None

    def get_authorize_url(self):

        params = {'redirect_uri': "http://localhost:8000/callback",
              'response_type': 'code'}

        url = self.service.get_authorize_url(**params)
        return url

    def configure_access_token(self, code):
        data = {'code': code,
                'redirect_uri': "http://localhost:8000/callback",
                'grant_type': 'authorization_code'}

        pt_auth_header = self.client_id + ':' + self.client_secret
        en_auth_header = base64.b64encode(pt_auth_header)
        headers = {'Authorization': "Basic " + en_auth_header}

        session = self.service.get_auth_session(data=data, headers=headers, decoder=json.loads)
        self.session = session
        access_token_response_body = self.service.access_token_response.json()
        self.access_token = access_token_response_body['access_token']

    def getData(self, params):
        headers = {'Authorization': "Bearer " + self.access_token}
        r = self.session.get('https://ohmage-omh.smalldata.io/dsu/dataPoints', params=params, headers=headers)
        return r

    def getPAMData(self, ios=True, created_on_or_after=None, created_before=None, skip=None, limit=100):

        if(ios):
            params = {'schema_namespace' : 'cornell',
                        'schema_name' : 'photographic-affect-meter-scores',
                        'schema_version' : '1.0',
                        'limit' : str(limit) }
        else:
            params = {'schema_namespace' : 'omh',
                        'schema_name' : 'pam',
                        'schema_version' : '1.0',
                        'limit' : str(limit) }


        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)

    def getMobilityDailySummaryData(self, created_on_or_after=None, created_before=None, skip=None, limit=100):

        params = {'schema_namespace' : 'cornell',
                    'schema_name' : 'mobility-daily-summary',
                    'schema_version' : '1.0',
                    'limit' : str(limit) }

        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)

    def getMobilityDailySegmentsData(self, created_on_or_after=None, created_before=None, skip=None, limit=100):

        params = {'schema_namespace' : 'cornell',
                    'schema_name' : 'mobility-daily-segments',
                    'schema_version' : '1.0',
                    'limit' : str(limit) }

        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)

    def getAndroidMobilitySensorData(self, created_on_or_after=None, created_before=None, skip=None, limit=100):

        params = {'schema_namespace' : 'omh',
                    'schema_name' : 'mobility',
                    'schema_version' : '1.0',
                    'limit' : str(limit) }

        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)

    def getAndroidLocationSensorData(self, created_on_or_after=None, created_before=None, skip=None, limit=100):

        params = {'schema_namespace' : 'omh',
                    'schema_name' : 'location',
                    'schema_version' : '1.0',
                    'limit' : str(limit) }

        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)

    def getIOSSensorData(self, created_on_or_after=None, created_before=None, skip=None, limit=100):

        params = {'schema_namespace' : 'cornell',
                    'schema_name' : 'mobility-stream-iOS',
                    'schema_version' : '1.0',
                    'limit' : str(limit) }

        if(created_on_or_after):
            params['created_on_or_after'] = created_on_or_after
        if(created_before):
            params['created_before'] = created_before
        if(skip):
            params['skip'] = str(skip)

        return self.getData(params)
