from flask.views import View
from flask import Response
from bson import json_util
from bson.son import SON

import pylev
import flask_pymongo

from adm import mongo

class SimilarCompanies(View):

    def dispatch_request(self):
        companies = mongo.db.procurements.aggregate([
            {   
                '$group': {
                    '_id': '$kompania.emri'
                }
            },
            {
                '$sort': SON([
                    ('_id', flask_pymongo.ASCENDING)
                ])
            }
        ])
        

        similarities = {}

        for idx1, company1 in enumerate(companies['result']):
            name1 = company1['_id']

            if name1 != None:
                if idx1 < len(companies['result']):
                    for idx2, company2 in enumerate(companies['result'][(idx1+1):]):
                        name2 = company2['_id']

                        if name2 != None:
                            if self.similar_sevenshtein(name1, name2):
                                #print 'Similarity detected: ' + str(name1) + ' - ' + str(name2)
                                
                                company2['_id'] = None;

                                if name1 in similarities:
                                    similarities[name1].append(name2)
                                else:
                                    similarities[name1] = [name2]


        # Build response object.
        resp = Response(
            response=json_util.dumps(similarities), mimetype='application/json')

        # Return response.
        return resp

    def similar_sevenshtein(self, string1, string2):
        return (pylev.levenshtein(string1, string2) <= 5)