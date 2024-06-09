# from datetime import datetime
# from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login, logout 
# def authenticateSession(request):
#     if request.user.is_authenticated:
#         current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         last_activity = request.session.get('last_activity', None)
#         if last_activity:
#                 ast_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
#                 if (datetime.datetime.now() - last_activity).seconds > 30: # 30 seconds = timeout duration
#                     logout(request)        
#     else:        
#         redirect('login')



# # import datetime
# # from django.contrib.auth import logout

# # class SessionTimeoutMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         if request.user.is_authenticated:
# #             current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# #             last_activity = request.session.get('last_activity', None)
# #             if last_activity:
# #                 last_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
# #                 if (datetime.datetime.now() - last_activity).seconds > 30: # 30 seconds = timeout duration
# #                     logout(request)
# #             request.session['last_activity'] = current_time
# #         response = self.get_response(request)
# #         return response