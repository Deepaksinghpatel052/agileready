
$(document).on("click",".get_help_conte",function(){


var geturl = window.location.href;
var url_in_array = geturl.split(base_url);
var page_name = url_in_array[1];

$.ajax({
	method:"POST",
	url:base_url+"account/get_help_content",
	data:{"page_name":page_name},
	dataType:"html",
	success:function(data)
	{
		// console.log(data);
		$("#help1 .modal-body").html(data);
	}
});


});





$(document).on("click",".get_help2_conte",function(){

	var geturl = window.location.href;
	var url_in_array = geturl.split(base_url);
	var page_name = "Product-Version-Notice";
	
	$.ajax({
		method:"POST",
		url:base_url+"account/get_help_content",
		data:{"page_name":page_name},
		dataType:"html",
		success:function(data)
		{
			// console.log(data);
			$("#help2 .modal-body").html(data);
		}
	});
	
	
	});


	$(document).on("click",".get_help3_conte",function(){

		var geturl = window.location.href;
		var url_in_array = geturl.split(base_url);
		var page_name = "ar-academy-link";
		
		$.ajax({
			method:"POST",
			url:base_url+"account/get_help_content",
			data:{"page_name":page_name},
			dataType:"html",
			success:function(data)
			{
				// console.log(data);
				$("#help3 .modal-body").html(data);
			}
		});
		
		
		});	


$(document).ready(function(){

var geturl = window.location.href;

var url_in_array = geturl.split("/");

// console.log(url_in_array);
var for_enver = false;
var for_manage_user = false;
var for_dashboard = false;
var for_exchange = false;



$(".sidebar-menu li a").each(function(){
	
console.log($(this).data("page"));
	switch($(this).data("page"))
    {
    	case "manage_products" :
        if(jQuery.inArray("manage-products", url_in_array) != -1) 
        {
        	 $(this).addClass('active');
        	 $("#page_name").html('Manage Products')
        	 // $('#show_col').css('display', 'none');
        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Manage Products">');

        	 for_enver = true;
        }
        
      	break; // break is optional
      	case "manage_features" :
	      	 if(jQuery.inArray("manage-feature", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Manage Feature">');

	        	 for_enver = true;
	        }
	      break;  
	    case "manage_epic_capability" :
	      	 if(jQuery.inArray("manage-epic-capabilities", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Epic Capabilities" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;   
       case "manage_team" :
	      	 if(jQuery.inArray("manage-team", url_in_array) != -1|| jQuery.inArray("manage-team#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Team" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;  
	    case "manage_backlogs" :
	      	 if(jQuery.inArray("manage-backlog", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('Manage Backlog');
	        	 // $('#show_col').css('display', 'none');
	        	 $("#feed").html('<input type="text" value="Manage Backlog" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
	    case "manage_iterations" :
	      	 if(jQuery.inArray("manage-iteration", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('Manage Iteration');
	        	 // $('#show_col').css('display', 'none');
	        	 $("#feed").html('<input type="text" value="Manage Iteration" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break; 
	    case "manage_team_member" :
	      	 if(jQuery.inArray("manage-team-member", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Team Member" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;

	    case "manage_goals" :
	      	 if(jQuery.inArray("manage-goals", url_in_array) != -1 || jQuery.inArray("manage-goals#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Goal" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;


	    case "manage_roles" :
	      	 if(jQuery.inArray("manage-role", url_in_array) != -1 || jQuery.inArray("manage-role#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Roles" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;

        case "manage_benefits" :
	      	 if(jQuery.inArray("manage-benefits", url_in_array) != -1 || jQuery.inArray("manage-benefits#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Benefits" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
// ----------------------------------------------------------------------

        case "manage_jobmot_set" :
	      	 if(jQuery.inArray("manage-jobmot-set", url_in_array) != -1 || jQuery.inArray("manage-jobmot-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Job Motivation Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "manage_joboutc_set" :
	      	 if(jQuery.inArray("manage-joboutc-set", url_in_array) != -1 || jQuery.inArray("manage-joboutc-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Job Outcome Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "manage_jobsit_set" :
	      	 if(jQuery.inArray("manage-jobsit-set", url_in_array) != -1 || jQuery.inArray("manage-jobsit-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Job Situation Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "manage_testact_set" :
	      	 if(jQuery.inArray("manage-testact-set", url_in_array) != -1 || jQuery.inArray("manage-testact-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Test Action Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "manage_testcond_set" :
	      	 if(jQuery.inArray("manage-testcond-set", url_in_array) != -1 || jQuery.inArray("manage-testcond-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Test Condition Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "manage_testoutc_set" :
	      	 if(jQuery.inArray("manage-testoutc-set", url_in_array) != -1 || jQuery.inArray("manage-testoutc-set#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Test Outcome Set" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
        case "business_value" :
	      	 if(jQuery.inArray("business-value", url_in_array) != -1 || jQuery.inArray("business-value#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Business Value" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;

// ----------------------------------------------------------------------
	    case "manage_user_story_point" :
	      	 if(jQuery.inArray("story-points", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Story Point" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;    
	   case "invite_new_user" :
	      	 if(jQuery.inArray("invite-user", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Invite User" class="form-control" readonly="" name="feedback_page">');
	        	 for_manage_user = true;
	        }
	      break;
	      case "manage_user_profile" :
	      	 if(jQuery.inArray("user-profile", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="User Profile" class="form-control" readonly="" name="feedback_page">');
	        	 for_manage_user = true;
	        }
	      break;
	   	case "dashboard":
	      	 if(jQuery.inArray("dashboard", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Dashboard" class="form-control" readonly="" name="feedback_page">');
	        	 for_dashboard = true;
	        }
	      break; 
	      case "user_story_view":
	      	 if(jQuery.inArray("user-story-view", url_in_array) != -1 || jQuery.inArray("user-story-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="User Story View">');

	        	 for_dashboard = true;
	        }
	        break; 
	      case "job_story_view":
	      	 if(jQuery.inArray("job-story-view", url_in_array) != -1 || jQuery.inArray("job-story-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Job Story View">');

	        	 for_dashboard = true;
	        }
	        break; 
	      case "bdd_tdd_story_view":
	      	 if(jQuery.inArray("bdd-tdd-story-view", url_in_array) != -1 || jQuery.inArray("bdd-tdd-story-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="BDD TDD Story View">');

	        	 for_dashboard = true;
	        }
	      break;
	      case "product_view":
	      	 if(jQuery.inArray("products-view", url_in_array) != -1 || jQuery.inArray("products-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('View Products')
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Product View">');

	        	 for_dashboard = true;
	        }
	      break;
	              case "manage_scenario" :
	      	 if(jQuery.inArray("manage-scenario", url_in_array) != -1 || jQuery.inArray("manage-scenario#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Scenario" class="form-control" readonly="" name="feedback_page">');
	        	 for_dashboard = true;
	        }
	      break;
	      case "words_patterns" :
	      	 if(jQuery.inArray("words-patterns", url_in_array) != -1 || jQuery.inArray("words-patterns#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Words and Patterns" class="form-control" readonly="" name="feedback_page">');
	        	 for_dashboard = true;
	        }
	      break;

	      case "user_story_value" :
	      	 if(jQuery.inArray("user-story-value", url_in_array) != -1 || jQuery.inArray("user-story-value#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="User Story Value" class="form-control" readonly="" name="feedback_page">');
	        	 for_dashboard = true;
	        }
	      break;

	      case "feature_value" :
	      	 if(jQuery.inArray("feature-value", url_in_array) != -1 || jQuery.inArray("feature-value#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Feature Value" class="form-control" readonly="" name="feedback_page">');
	        	 for_dashboard = true;
	        }
	      break;

	      case "backlog_view":
	      	 if(jQuery.inArray("backlog-view", url_in_array) != -1 ) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('Backlog View')
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Backlog View">');

	        	 for_dashboard = true;
	        }
	      break;   
	      case "iteration_view":
	      	 if(jQuery.inArray("iteration-view", url_in_array) != -1 || jQuery.inArray("iteration-view#", url_in_array) != -1 ) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Iteration View">');
	        	 for_dashboard = true;
	        }
	      break;

	      case "manage_export_data" :
	      	 if(jQuery.inArray("export-data", url_in_array) != -1 || jQuery.inArray("export-data#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Export" class="form-control" readonly="" name="feedback_page">');
	        	 for_exchange = true;
	        }
	      break;

	      	      case "manage_import_data" :
	      	 if(jQuery.inArray("import-data", url_in_array) != -1 || jQuery.inArray("import-data#", url_in_array) != -1)
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage Import" class="form-control" readonly="" name="feedback_page">');
	        	 for_exchange = true;
	        }
	      break;      
        
     

    }
    if(for_enver)
    {
    	$(".nmanage_environment_menu").addClass("active");
        $(".manage_account_menu").addClass("active");
    }
    if(for_manage_user)
    {
        $(".manage_users_menu").addClass("active");
        $(".manage_account_menu").addClass("active");
    }

    if(for_exchange)
    {
        $(".data_exchange_menu").addClass("active");
        $(".manage_account_menu").addClass("active");
    }
    
    if(for_dashboard)
    {
    	$(".dashboard_menu").addClass("active");
    }
});

});