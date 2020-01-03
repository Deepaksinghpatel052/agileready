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
        	 for_enver = true;
        }
        
      	break; // break is optional
      	case "manage_features" :
	      	 if(jQuery.inArray("manage-feature", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_enver = true;
	        }
	      break;  
	    case "manage_epic_capability" :
	      	 if(jQuery.inArray("manage-epic-capabilities", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_enver = true;
	        }
	      break;   
       case "manage_team" :
	      	 if(jQuery.inArray("manage-team", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_enver = true;
	        }
	      break;  
	    case "manage_backlogs" :
	      	 if(jQuery.inArray("manage-backlog", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_enver = true;
	        }
	      break;    
	   case "invite_new_user" :
	      	 if(jQuery.inArray("invite-user", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_manage_user = true;
	        }
	      break; 
	   	case "dashboard":
	      	 if(jQuery.inArray("dashboard", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
	        	 for_dashboard = true;
	        }
	      break; 
	      case "user_story_view":
	      	 if(jQuery.inArray("user-story-view", url_in_array) != -1 || jQuery.inArray("user-story-view#", url_in_array) != -1) 
	        {
	        	 $(this).addClass('active');
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