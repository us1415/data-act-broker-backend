import requests
import json
import os
import inspect

class ManagerProxy(object):
    """ Temporary bypass of job manager, used to call validator directly """
    MANAGER_FILE  = "manager.json"
    JSON_HEADER = {"Content-Type": "application/json"}

    def _getPath(self,):
        """ Get path to validator out of JSON file """
        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        dirName, fileName = os.path.split(path)
        credFile = os.path.join(dirName, ManagerProxy.MANAGER_FILE)
        return json.loads(open(credFile,"r").read())["URL"]

    def jobJson(self,jobId):
        """ Create JSON to hold jobId """
        return '{"job_id":"'+str(jobId)+'"}'

    def sendJobRequest(self,jobId):
        """ Send request to validator """
        return requests.request(method="POST", url=self._getPath() + "/validate_threaded/", data=self.jobJson(jobId), headers = self.JSON_HEADER)

