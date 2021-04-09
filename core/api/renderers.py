from rest_framework.renderers import JSONRenderer


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_dict = {
            'status': True,
            'data': data,
        }
        # if data.get('status', False):
        #     response_dict['status'] = data.get('status')
        data = response_dict
        return super(ApiRenderer, self).render(data, accepted_media_type, renderer_context)
