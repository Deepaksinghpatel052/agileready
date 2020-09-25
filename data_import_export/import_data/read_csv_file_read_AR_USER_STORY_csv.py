import io,csv
from django.shortcuts import get_object_or_404
from user_story_points.models import ArUserStoryPoints
from datetime import datetime
from account.models import Ar_user,Notification
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
import string
import random
from agileproject import settings
from manage_backlogs.models import AR_BACKLOG
from user_story_view.models import AR_USER_STORY,AR_US_STATUS,AR_US_TYPE
from user_story_view.user_story_score.readiness_quality_score import quelity_score
from user_story_view.set_user_story_acceptance_criteria_and_conver_algo import flesch_reading_ease
from dashboard.views import get_package_limit

from django.contrib import messages

def read_AR_USER_STORY_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    created_by_ins = get_object_or_404(Ar_user, pk=user_id)
    updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)
    ar_user_set = get_object_or_404(Ar_user, pk=user_id)
    file_name = get_data
    i=2

    total = 0
    import_s = 0
    existss = 0
    empty = 0
    other_error = 0
    try:
        for item in file_name:
            # print("===")
            # print(len(item))
            # print("0:"+item[0]+"====1:"+item[1]+"====2:"+item[2]+"====3:"+item[3]+"====4:"+item[4]+"====5:"+item[5]+"====6:"+item[6]+"====7:"+item[7]+"====8:"+item[8]+"9:"+item[9]+"====10:"+item[10]+"====11"+item[11]+"====12:"+item[12]+"====13:"+item[13]+"====14:"+item[14]+"====15:"+item[15]+"====16:"+item[16]+"====17:"+item[17]+"====19:"+item[19]+"====20:"+item[20])
            # print("===")
            if item[0] == "":
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : user story title is empty. : " + str(datetime.now()) + "\r\n")
                empty += 1
            else:
                if AR_USER_STORY.objects.filter(title=item[0]).filter(ORG_id=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                    existss += 1
                else:
                    # backlog_parent Start
                    backlog_parent = None
                    print("===")
                    if item[5] != "":
                        try:
                            bl_id = int(item[5])
                            if AR_BACKLOG.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                backlog_parent = get_object_or_404(AR_BACKLOG, pk=bl_id)
                        except:
                            if AR_BACKLOG.objects.filter(title=item[5]).filter(ORG_ID=org_ins).exists():
                                backlog_parent = get_object_or_404(AR_BACKLOG, title=item[5], ORG_ID=org_ins)
                    # print(backlog_parent)

                    # backlog_parent END
                    if item[7] == "1":
                        autoscoring_on = True
                    else:
                        autoscoring_on = False

                    if item[8] == "1":
                        archive_indicator = True
                    else:
                        archive_indicator = False
                    # story_points_set Start
                    story_points_set = None
                    if item[10] != "":
                        try:
                            story_points_set_id = int(item[10])
                            if ArUserStoryPoints.objects.filter(id=story_points_set_id).filter(ORG_ID=org_ins).exists():
                                story_points_set = get_object_or_404(ArUserStoryPoints, pk=story_points_set_id)
                        except:
                            if ArUserStoryPoints.objects.filter(Point_Key=item[10]).filter(ORG_ID=org_ins).exists():
                                story_points_set = get_object_or_404(ArUserStoryPoints, Point_Key=item[10], ORG_ID=org_ins)
                    # print(story_points_set)
                    # story_points_set End

                    # ============user_story_status START
                    user_story_status_set = None
                    if item[11] != "":
                        try:
                            item_id = int(item[11])
                            if AR_US_STATUS.objects.filter(id=item_id).exists():
                                user_story_status_set = get_object_or_404(AR_US_STATUS, pk=item_id)
                        except:
                            if AR_US_STATUS.objects.filter(status_key=item[11]).exists():
                                user_story_status_set = get_object_or_404(AR_US_STATUS, status_key=item[11])
                    # print(user_story_status_set)
                    # ============user_story_status END

                    # ============UST_ID START
                    UST_ID_set = None
                    if item[12] != "":
                        try:
                            UST_ID_id = int(item[12])
                            if AR_US_TYPE.objects.filter(id=UST_ID_id).exists():
                                UST_ID_set = get_object_or_404(AR_US_TYPE, pk=UST_ID_id)
                        except:
                            if AR_US_TYPE.objects.filter(type_key=item[12]).exists():
                                UST_ID_set = get_object_or_404(AR_US_TYPE, type_key=item[12])
                    # print(UST_ID_set)
                    # ============UST_ID END

                    # =========ar_user Start
                    ar_user_set = None
                    if item[13] != "":
                        try:
                            ar_user_id = int(item[13])
                            if Ar_user.objects.filter(id=ar_user_id).filter(org_id=org_ins).exists():
                                ar_user_set = get_object_or_404(Ar_user, pk=ar_user_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                                ar_user_set = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)
                    # print(ar_user_set)
                    # =========ar_user END

                    # =========owner Start
                    owner = get_object_or_404(Ar_user, pk=user_id)
                    if item[14] != "":
                        try:
                            owner_id = int(item[14])
                            if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, pk=owner_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[14]).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, user_name=item[14], org_id=org_ins)
                    # print(owner)
                    # =========owner End

                    # ============== create_by update_by start
                    if item[15] != "":
                        try:
                            created_by_ins_id = int(item[15])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[15]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[15], org_id=org_ins)
                    if item[18] != "":
                        try:
                            updateded_by_ins_id = int(item[18])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[18]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[18], org_id=org_ins)
                    print(created_by_ins)
                    print(updateded_by_ins)
                    # ============== create_by update_by end

                    # CREATE_DT UPDATE_DT START
                    created_dt = datetime.now()
                    updated_dt = datetime.now()
                    # created_dt = item[16]
                    #
                    # if created_dt == "":
                    #     created_dt = datetime.now()
                    # updated_dt = item[17]
                    # if updated_dt == "":
                    #     updated_dt = datetime.now()
                    # CREATE_DT UPDATE_DT END

                    # set string to int start
                    ac_readability_score = 0
                    if item[2] != "":
                        ac_readability_score = flesch_reading_ease(item[2])

                    convo_readability_score = 0
                    if item[4] != "":
                        convo_readability_score = flesch_reading_ease(item[4])


                    readiness_quality_score = 0
                    readiness_quality_score_list = quelity_score(item[1])
                    readiness_quality_score = readiness_quality_score_list[0]
                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"
                    userStory = AR_USER_STORY(title=item[0],data_Type=set_dummy_data, story_tri_part_text=item[1], acceptance_criteria=item[2],
                                              ac_readability_score=ac_readability_score, conversation=item[4],
                                              backlog_parent=backlog_parent, convo_readability_score=convo_readability_score,
                                              autoscoring_on=autoscoring_on, archive_indicator=archive_indicator,
                                              readiness_quality_score=readiness_quality_score, story_points=story_points_set,
                                              user_story_status=user_story_status_set, ORG_id=org_ins, UST_ID=UST_ID_set,
                                              ar_user=ar_user_set, owner=owner, created_by=created_by_ins,
                                              updated_by=updateded_by_ins)
                    # userStory.save()

                    try:
                        get_status = get_package_limit(org_ins.id,"Backlogs")

                        if set_dummy_data == "Dommy Data":
                              get_status =True

                        if get_status:
                            userStory.save()
                            msg_data = get_object_or_404(Notification, page_name="User Story View", notification_key="Add")
                            file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                            import_s += 1
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(item[0]) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Subscription limit expiry date. : " + str(datetime.now()) + "\r\n")
                    except Exception as e:
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
                        other_error += 1
                    # print("===")
            i += 1
            total += 1
            upload_status_set = True
    except Exception as e:
        upload_status_set = False
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " :  "+str(e)+" : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    if existss > 0:
        exisis = str(existss) + " story exists.,,"
    else:
        exisis = ''
    if empty > 0:
        empty_msg = str(empty)+" story title is emptys.,,"
    else:
        empty_msg = ''
    file_data = str(total)+" total user story.,,"+str(import_s)+" story import.,,"+empty_msg+exisis+str(other_error)+" other error"

    # -------------------------------------------------
    if set_data_type== "default" :
        pass
    else:
        if import_s == 0 :
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="import_error")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        else:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
    # -------------------------------------------------
    import_files_data.objects.filter(id=file_ins.id).update(error_log=file_name_txt_in_array[1],file_data=file_data,upload_status=upload_status_set)
    return True




# =========================================================================================

def read_AR_USER_STORY_csv_test(file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    created_by_ins = get_object_or_404(Ar_user, pk=user_id)
    updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)
    ar_user_set = get_object_or_404(Ar_user, pk=user_id)
    file_name = get_data
    i=2

    total = 0
    import_s = 0
    existss = 0
    empty = 0
    other_error = 0
    # try:
    for item in file_name:
        if item[0] == "":
            file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : user story title is empty. : " + str(datetime.now()) + "\r\n")
            empty += 1
        else:
            if AR_USER_STORY.objects.filter(title=item[0]).filter(ORG_id=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Exists")
                msg_data = msg.notification_desc
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                existss += 1
            else:
                # backlog_parent Start
                backlog_parent = None
                print("===")
                if item[5] != "":
                    try:
                        bl_id = int(item[5])
                        if AR_BACKLOG.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                            backlog_parent = get_object_or_404(AR_BACKLOG, pk=bl_id)
                    except:
                        if AR_BACKLOG.objects.filter(title=item[5]).filter(ORG_ID=org_ins).exists():
                            backlog_parent = get_object_or_404(AR_BACKLOG, title=item[5], ORG_ID=org_ins)
                # print(backlog_parent)

                # backlog_parent END
                if item[7] == "1":
                    autoscoring_on = True
                else:
                    autoscoring_on = False

                if item[8] == "1":
                    archive_indicator = True
                else:
                    archive_indicator = False
                # story_points_set Start
                story_points_set = None
                if item[10] != "":
                    try:
                        story_points_set_id = int(item[10])
                        if ArUserStoryPoints.objects.filter(id=story_points_set_id).filter(ORG_ID=org_ins).exists():
                            story_points_set = get_object_or_404(ArUserStoryPoints, pk=story_points_set_id)
                    except:
                        if ArUserStoryPoints.objects.filter(Point_Key=item[10]).filter(ORG_ID=org_ins).exists():
                            story_points_set = get_object_or_404(ArUserStoryPoints, Point_Key=item[10], ORG_ID=org_ins)
                # print(story_points_set)
                # story_points_set End

                # ============user_story_status START
                user_story_status_set = None
                if item[11] != "":
                    try:
                        item_id = int(item[11])
                        if AR_US_STATUS.objects.filter(id=item_id).exists():
                            user_story_status_set = get_object_or_404(AR_US_STATUS, pk=item_id)
                    except:
                        if AR_US_STATUS.objects.filter(status_key=item[11]).exists():
                            user_story_status_set = get_object_or_404(AR_US_STATUS, status_key=item[11])
                # print(user_story_status_set)
                # ============user_story_status END

                # ============UST_ID START
                UST_ID_set = None
                if item[12] != "":
                    try:
                        UST_ID_id = int(item[12])
                        if AR_US_TYPE.objects.filter(id=UST_ID_id).exists():
                            UST_ID_set = get_object_or_404(AR_US_TYPE, pk=UST_ID_id)
                    except:
                        if AR_US_TYPE.objects.filter(type_key=item[12]).exists():
                            UST_ID_set = get_object_or_404(AR_US_TYPE, type_key=item[12])
                # print(UST_ID_set)
                # ============UST_ID END

                # =========ar_user Start
                ar_user_set = None
                if item[13] != "":
                    try:
                        ar_user_id = int(item[13])
                        if Ar_user.objects.filter(id=ar_user_id).filter(org_id=org_ins).exists():
                            ar_user_set = get_object_or_404(Ar_user, pk=ar_user_id)
                    except:
                        if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                            ar_user_set = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)
                # print(ar_user_set)
                # =========ar_user END

                # =========owner Start
                owner = get_object_or_404(Ar_user, pk=user_id)
                if item[14] != "":
                    try:
                        owner_id = int(item[14])
                        if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                            owner = get_object_or_404(Ar_user, pk=owner_id)
                    except:
                        if Ar_user.objects.filter(user_name=item[14]).filter(org_id=org_ins).exists():
                            owner = get_object_or_404(Ar_user, user_name=item[14], org_id=org_ins)
                # print(owner)
                # =========owner End

                # ============== create_by update_by start
                if item[15] != "":
                    try:
                        created_by_ins_id = int(item[15])
                        if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                            created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                    except:
                        if Ar_user.objects.filter(user_name=item[15]).filter(org_id=org_ins).exists():
                            created_by_ins = get_object_or_404(Ar_user, user_name=item[15], org_id=org_ins)
                if item[18] != "":
                    try:
                        updateded_by_ins_id = int(item[18])
                        if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                            updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                    except:
                        if Ar_user.objects.filter(user_name=item[18]).filter(org_id=org_ins).exists():
                            updateded_by_ins = get_object_or_404(Ar_user, user_name=item[18], org_id=org_ins)
                print(created_by_ins)
                print(updateded_by_ins)
                # ============== create_by update_by end

                # CREATE_DT UPDATE_DT START
                created_dt = datetime.now()
                updated_dt = datetime.now()
                # created_dt = item[16]
                #
                # if created_dt == "":
                #     created_dt = datetime.now()
                # updated_dt = item[17]
                # if updated_dt == "":
                #     updated_dt = datetime.now()
                # CREATE_DT UPDATE_DT END

                # set string to int start
                ac_readability_score = 0
                if item[2] != "":
                    ac_readability_score = flesch_reading_ease(item[2])

                convo_readability_score = 0
                if item[4] != "":
                    convo_readability_score = flesch_reading_ease(item[4])


                readiness_quality_score = 0
                readiness_quality_score_list = quelity_score(item[1])
                readiness_quality_score = readiness_quality_score_list[0]
                if set_dummy_data == "":
                    set_dummy_data = "ORG Data"
                userStory = AR_USER_STORY(title=item[0],data_Type=set_dummy_data, story_tri_part_text=item[1], acceptance_criteria=item[2],
                                              ac_readability_score=ac_readability_score, conversation=item[4],
                                              backlog_parent=backlog_parent, convo_readability_score=convo_readability_score,
                                              autoscoring_on=autoscoring_on, archive_indicator=archive_indicator,
                                              readiness_quality_score=readiness_quality_score, story_points=story_points_set,
                                              user_story_status=user_story_status_set, ORG_id=org_ins, UST_ID=UST_ID_set,
                                              ar_user=ar_user_set, owner=owner, created_by=created_by_ins,
                                              updated_by=updateded_by_ins)
                # userStory.save()

                try:
                    get_status = get_package_limit(org_ins.id,"Backlogs")
                        
                    if set_dummy_data == "Dommy Data":
                            get_status =True
                              
                    if get_status:
                        userStory.save()
                        msg_data = get_object_or_404(Notification, page_name="User Story View", notification_key="Add")
                        file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                        import_s += 1
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        file2.write("Error : " + str(item[0]) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Subscription limit expiry. : " + str(datetime.now()) + "\r\n")
                except:
                    file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Something was wrong in this file : " + str(datetime.now()) + "\r\n")
                    other_error += 1
                # print("===")
        i += 1
        total += 1
        upload_status_set = True
    # except Exception as e:
    #     upload_status_set = False
    #     print("===============================================================")
    #     print(e)
    #     print("=============================================================")
    #     file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Something was wrong in this file.(Ar) : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    if existss > 0:
        exisis = str(existss) + " story exists.,,"
    else:
        exisis = ''
    if empty > 0:
        empty_msg = str(empty)+" story title is emptys.,,"
    else:
        empty_msg = ''
    file_data = str(total)+" total user story.,,"+str(import_s)+" story import.,,"+empty_msg+exisis+str(other_error)+" other error"

    import_files_data.objects.filter(id=file_ins.id).update(error_log=file_name_txt_in_array[1],file_data=file_data,upload_status=upload_status_set)
    return True
