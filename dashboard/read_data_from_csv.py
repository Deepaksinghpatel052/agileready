from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User,auth
from agileproject import settings
from account.models import AR_organization,csvFilesUplodaded,Notification
from manage_product.models import AR_product,AR_team,Ar_user
from manage_backlogs.models import AR_BACKLOG,AR_BACKLOG_STATUS
from user_story_view.models import AR_USER_STORY
from manage_iterations.models import ArIterations
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
import csv, io



def read_csv_files_data(file_id,org_id,user_id):
    file_id = file_id
    message = "work fine"
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded,pk=file_id)
        if get_files.ORG_ID.id != org_id:
            message = "This CSV file is not related to your organization."
        else:
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            file_name = get_data
            get_names = ""
            created_by_ins = get_object_or_404(Ar_user, pk=user_id)
            updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)
            org_ins = get_object_or_404(AR_organization, pk=org_id)
            for item in file_name:

                # ======================== CODE FOR PRODUCT START ============================
                if get_files.csvUseFor == 'Ar Product':
                    # item[0]  product name
                    # item[1]  product description
                    # item[2]  Business_unit
                    # item[3]  US_quality_threshold
                    # item[4]  Createed_by
                    # item[5]  created_date
                    # item[6]  Updateded_by
                    # item[7]  Updated_date

                    if item[0] != '':
                        if AR_product.objects.filter(Product_name=item[0]).filter(ORG_ID=org_ins).exists():
                            msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Exists")
                            msg_data = msg.notification_desc
                            messages.error(request, msg_data)
                        else:
                            if Ar_user.objects.filter(id=item[4]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=item[4])
                            if Ar_user.objects.filter(user_name=item[4]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[4],org_id=org_ins)

                            if Ar_user.objects.filter(id=item[6]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=item[6])
                            if Ar_user.objects.filter(user_name=item[6]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[6],org_id=org_ins)

                            data = AR_product(Product_name=item[0], Product_description=item[1], Business_unit=item[2],US_quality_threshold=item[3],ORG_ID=org_ins,create_by=created_by_ins, update_by=updateded_by_ins)
                            data.save()
                # ======================== CODE FOR PRODUCT END ============================

                # ======================== CODE FOR BACKLOG START ============================
                if get_files.csvUseFor == 'Ar Backlog':
                    # item[0]  backlog title
                    # item[1]  owner
                    # item[2]  Team list
                    # item[3]  product_paren
                    # item[4]  BL_STATUS
                    # item[5]  created_by
                    # item[6]  created_dt
                    # item[7]  Updated_by
                    # item[8]  Updated_date
                    # product_paren = ""
                    if item[0] != '':
                        if AR_BACKLOG.objects.filter(title=item[0]).filter(ORG_ID=org_ins).exists():
                            msg = get_object_or_404(Notification, page_name="Manage Backlog", notification_key="Exists")
                            msg_data = msg.notification_desc
                            messages.error(request, msg_data)
                        else:
                            owner = get_object_or_404(Ar_user, pk=user_id)
                            if item[1] != "":
                                if Ar_user.objects.filter(id=item[1]).filter(org_id=org_ins).exists():
                                    owner = get_object_or_404(Ar_user, pk=item[1])
                                if Ar_user.objects.filter(user_name=item[1]).filter(org_id=org_ins).exists():
                                    owner = get_object_or_404(Ar_user, user_name=item[1],org_id=org_ins)
                            if item[3] == "":
                                product_paren = None
                            else:
                                product_paren = get_object_or_404(AR_product, pk=item[3])
                                #==== GET PRODUCT INSTANCE
                                if AR_product.objects.filter(id=item[3]).filter(ORG_ID=org_ins).exists():
                                    product_paren = get_object_or_404(AR_product, pk=item[3])
                                if AR_product.objects.filter(Product_name=item[3]).filter(ORG_ID=org_ins).exists():
                                    product_paren = get_object_or_404(AR_product, Product_name=item[3],ORG_ID=org_ins)

                            # ==== GET BACKLOG STATUS INSTANCE
                            if item[4] == "":
                                bl_status = None
                            else:
                                if AR_BACKLOG_STATUS.objects.filter(id=item[4]).exists():
                                    bl_status = get_object_or_404(AR_BACKLOG_STATUS, pk=item[4])
                                if AR_BACKLOG_STATUS.objects.filter(bl_status_key=item[4]).exists():
                                    bl_status = get_object_or_404(AR_BACKLOG_STATUS, bl_status_key=item[4])

                            if Ar_user.objects.filter(id=item[5]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=item[5])
                            if Ar_user.objects.filter(user_name=item[5]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[5], org_id=org_ins)

                            if Ar_user.objects.filter(id=item[7]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=item[7])
                            if Ar_user.objects.filter(user_name=item[7]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[7], org_id=org_ins)
                            backlog_score = 0
                            Backlog_size = 0

                            if item[2] == "":
                                set_team = None
                            else:
                                team_in_list = item[2].split("|")
                                set_team = AR_team.objects.filter(id__in=team_in_list).filter(ORG_id=org_ins)
                            data_set = AR_BACKLOG(title=item[0],backlog_score=backlog_score,Backlog_size=Backlog_size,owner=owner,product_parent=product_paren,BL_STATUS=bl_status,ORG_ID=org_ins,created_by=created_by_ins,updated_by=updateded_by_ins)
                            data_set.save()
                            if set_team != None:
                                data_set.team_list.set(set_team)

                # ======================== CODE FOR BACKLOG END ============================


            messages.info(request, "data Import Successfully.")
            return HttpResponse(get_names)
    else:
        message = "Data not found"
    return HttpResponse(message)
