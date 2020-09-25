$(document).ready(function(){

var geturl = window.location.href;

var url_in_array = geturl.split("/");

// console.log(url_in_array);
var for_enver = false;
var for_manage_user = false;
var for_dashboard = false;
$(".sidebar-menu li a").each(function(){
	
console.log($(this).data("page"))
	switch($(this).data("page"))
    {
    	case "manage_products" :
        if(jQuery.inArray("manage-products", url_in_array) != -1) 
        {
        	 $(this).addClass('active');
        	 $("#page_name").html('Manage Products')
        	 $('#show_col').css('display', 'none');
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
	      	 if(jQuery.inArray("manage-team", url_in_array) != -1) 
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
	        	 $('#show_col').css('display', 'none');
	        	 $("#feed").html('<input type="text" value="Manage Backlog" class="form-control" readonly="" name="feedback_page">');
	        	 for_enver = true;
	        }
	      break;
	    case "manage_iterations" :
	      	 if(jQuery.inArray("manage-iteration", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('Manage Iteration');
	        	 $('#show_col').css('display', 'none');
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
	    case "manage_user_story_point" :
	      	 if(jQuery.inArray("user-story-points", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" value="Manage User Story Point" class="form-control" readonly="" name="feedback_page">');
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
	      case "product_view":
	      	 if(jQuery.inArray("products-view", url_in_array) != -1 || jQuery.inArray("products-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 $("#page_name").html('View Products')
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Product View">');

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
	      	 if(jQuery.inArray("iteration-view", url_in_array) != -1 ) 
	        {
	        	 $(this).addClass('active');
	        	 $("#feed").html('<input type="text" class="form-control" readonly="" name="feedback_page" value="Iteration View">');
	        	 for_dashboard = true;
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
    if(for_dashboard)
    {
    	$(".dashboard_menu").addClass("active");
    }
});

});