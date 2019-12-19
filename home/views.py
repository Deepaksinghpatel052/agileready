from django.shortcuts import render
from django.conf import settings
# from account.forms import User_Form,AR_USER_Form
from django.core.mail import send_mail
import smtplib
import email.message
# Create your views here.

def login_page(request):
    return render(request, 'web/home/index.html', {'home_active': "active", 'BASE_URL': settings.BASE_URL,"set_login":"do_login"})


def index(request):
    # 'user_form': User_Form, 'ar_user_form': AR_USER_Form,
    # if 'user_email' in request.session:
    #     return render(request, 'dashboard/dashboard_user/dashboard.html', {"message": "Logged in Successfully"})
    return render(request, 'web/home/index.html', {'home_active': "active", 'BASE_URL':settings.BASE_URL})

def whyar(request):
    return render(request, 'web/why-agile-ready/index.html', {'whyar_active': "active", 'BASE_URL':settings.BASE_URL})


def company(request):

#     message = """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="utf-8">
# <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
# <meta name="description" content="">
# <meta name="author" content="">
# <link rel="icon" href="assets/img/basic/favicon.png" type="image/x-icon">
# <title>Agile | Home</title>
# <link href="https://fonts.googleapis.com/css?family=Roboto:400,500&display=swap" rel="stylesheet">
# <link rel="stylesheet" href="assets/css/app.css">
# <link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
# </head>
# <body>
# <div id="app">
#    <div class="nav-sticky white">
#       <nav class="mainnav navbar navbar-default justify-content-between">
#          <div class="container relative" style="display: flex;"><a class="offcanvas dl-trigger paper-nav-toggle" type="button" data-toggle="offcanvas" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><i></i></a> <a class="navbar-brand" href="index.html"><img class="d-inline-block align-top" alt="" src="assets/img/basic/logo2.png"></a>
#             <div class="paper_menu">
#                <div id="dl-menu" class="xv-menuwrapper responsive-menu">
#                   <ul class="dl-menu align-items-center">
#                      <li class="parent"><a class="active" href="index.html">Home</a></li>
#                      <li class="parent"><a href="ar-whyar.html">Why Agile Ready</a>
#                      </li>
#                      <li class="parent"><a href="ar-company.html">Company</a></li>
#                      <li class="parent"><a href="subscription.html">Subscriptions</a></li>
#                      </li>
#                      <li class="parent"><a href="ar-usrating.html">User Story Rating</a>
#                      </li>
#                      <li> <a href="dashboard.html" data-toggle="modal" class="btn btn-primary nav-btn" data-target="#modalLogin">Sign In</a></li>
#                      <!-- <li><a href="dashboard.html" class="btn btn-primary nav-btn" data-toggle="modal" data-target="#modalSignUp">Sign Up</a></li> -->
#                   </ul>
#                </div>
#             </div>
#          </div>
#       </nav>
#    </div>
#    <main>
#       <section class="p-t-b-40 animatedParent animateOnce responsive">
#          <div class="container">
#             <div class="row">
#                   <div class="col-lg-12"><form action="dashboard.html">
#                   <div class="col-lg-12">
#                      <div class="p-t-b-40">
#                         <div class="p-10">
#                            <h2 class="p-b-20 text-center">Invited User Account</h2>
#                               <div class="row"><div class="col-md-6 float-left"><div class="form-group has-icon"><i class="icon-user-circle"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Your Name">
#                               </div></div>
#                               <div class="col-md-6 float-right"><div class="form-group has-icon"><i class="icon-envelope-o"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Email Address">
#                               </div></div></div>
#                        <div class="row"><div class="col-md-6 float-left"><div class="form-group has-icon"><i class="icon-user-circle"></i>
#                                  <input type="password" class="form-control form-control-lg" placeholder="Password">
#                               </div></div>
#                               <div class="col-md-6 float-right"><div class="form-group has-icon"><i class="icon-envelope-o"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Your City">
#                               </div></div></div>
#                        <div class="row"><div class="col-md-6 float-left"><div class="form-group has-icon"><i class="icon-user-circle"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Your state">
#                               </div></div>
#                               <div class="col-md-6 float-right"><div class="form-group has-icon"><i class="icon-envelope-o"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Zip code">
#                               </div></div></div>
#                        <div class="row"><div class="col-md-6 float-left"><div class="form-group has-icon"><i class="icon-user-circle"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Country">
#                               </div></div>
#                               <div class="col-md-6 float-right"><div class="form-group has-icon"><i class="icon-envelope-o"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Phone number">
#                               </div></div></div>
#                               <div class="row"><div class="col-md-6 float-left"><div class="form-group has-icon"><i class="icon-user-circle"></i>
#                                  <input type="text" class="form-control form-control-lg" placeholder="Company">
#                               </div></div></div>
#                        <div class="row">
#                               <div class="col-md-4 offset-md-4"><input type="submit" class="btn btn-primary btn-lg btn-block" value="Sign Up Now"></div>
#                        </div>
#                         </div>
#                      </div>
#                   </div>
#               </form>
#                </div></div>
#          </div>
#       </section>
#    </main>
#    <footer>
#       <section class="p-t-b-20 service-blocks animatedParent animateOnce">
#       <div class="container">
#          <div class="row">
#             <!-- <div class=" col-lg-2 col-xl-3 col-12 responsive-phone"> <a href="#" class="brand"><img src="assets/img/basic/logo.png" alt="Knowledge"><span class="circle"></span></a></div> -->
#          <!-- <div class="container">
#             <div class="row"> -->
#                <div class="col-lg-4 ">
#                   <div class="service-block clearfix">
#                      <div class="service-icon"><i class="icon icon-dollar"></i></div>
#                      <div class="service-content">
#                         <h3><a href="#">Reduce User Story Lifecycle Costs</a></h3>
#                         <p>Drop your user story lifecycle costs 33% to 70%. Save time (thus money) getting stories ready faster.</p>
#                      </div>
#                   </div>
#                </div>
#                <div class="col-lg-4">
#                   <div class="service-block">
#                      <div class="service-icon"><i class="icon icon-graduation"></i></div>
#                      <div class="service-content">
#                         <h3><a href="#">Save on Training Costs</a></h3>
#                         <p>On-Board new Product Owners faster. Continuous rating system feedback tutors everyone on good user story writing.</p>
#                      </div>
#                   </div>
#                </div>
#                <div class="col-lg-4">
#                   <div class="service-block clearfix">
#                      <div class="service-icon"><i class="icon icon-cloud-upload"></i></div>
#                      <div class="service-content">
#                         <h3><a href="#">Import/Export</a></h3>
#                         <p>Import user stories and rate them. Export Backlogs and their user stories. Export to external systems such as Rally, Jira and VersionOne.</p>
#                      </div>
#                   </div>
#                </div>
#            <!--  </div>
#          </div> -->
#          </div>
#       </div>
#    </section>
#    </footer>
#    <div class="modal fade" id="modalLogin" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
#       <div class="modal-dialog width-400" role="document">
#          <div class="modal-content no-r "><a href="#" data-dismiss="modal" aria-label="Close" class="paper-nav-toggle active"><i></i></a>
#             <div class="modal-body no-p">
#                <div class="text-center p-40 p-b-0"> <img src="assets/img/dummy/u4.png" alt="">
#                   <h2 class=" text-center">Login</h2>
#                </div>
#                <div class="light p-40">
#                   <form action="dashboard.html">
#                      <div class="form-group has-icon"><i class="icon-envelope-o"></i>
#                         <input type="text" class="form-control form-control-lg" placeholder="Email Address">
#                      </div>
#                      <div class="form-group has-icon"><i class="icon-user-secret"></i>
#                         <input type="text" class="form-control form-control-lg" placeholder="Password">
#                      </div>
#                      <input type="submit" class="btn btn-primary btn-lg btn-block" value="Log In">
#                      <small class="forget-pass">Have you forgot your username or password ?</small>
#                   </form>
#                </div>
#             </div>
#          </div>
#       </div>
#    </div>
#    <div class="modal fade" id="modalSignUp" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
#       <div class="modal-dialog modal-lg" role="document">
#          <div class="modal-content no-r "><a href="#" data-dismiss="modal" aria-label="Close" class="paper-nav-toggle active"><i></i></a>
#             <div class="modal-body no-p">
#             </div>
#          </div>
#       </div>
#    </div>
# </div>
# <script src="assets/js/app.js"></script>
# </body>
# </html>
#     """
#     msg = email.message.Message()
#     msg['Subject'] = 'HTML Document'
#     password = settings.EMAIL_HOST_PASSWORD
#     msg['From'] = settings.EMAIL_HOST_USER
#     msg['To'] = 'ram.gautam@digimonk.in'
#     msg.add_header('Content-Type', 'text/html')
#     msg.set_payload(message)
#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()
#     # Login Credentials for sending the mail
#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string())

    return render(request, 'web/company/index.html', {'company_active': "active", 'BASE_URL':settings.BASE_URL})


def subscription(request):
    return render(request, 'web/subscriptions/index.html', {'subscription_active': "active", 'BASE_URL':settings.BASE_URL})


def usrating(request):
    return render(request, 'web/user-story-rating/index.html', {'usrating_active': "active", 'BASE_URL':settings.BASE_URL})




# def dashboard(request):
#     del request.session['user_email']
#     return render(request, 'basic/index.html', {'company_active': "active"})
