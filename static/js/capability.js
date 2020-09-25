$(document).ready(function(){

$("#id_PROJECT_ID").change(function(){
var ids=$(this).val();
get_capanility_according_to_product(ids);
 
});

});


function get_capanility_according_to_product(product_id)
{

   if(product_id !="")
   {

	$.ajax({
      method:"GET",
      url : base_url+"manage-epic-capabilities/get_capanility/"+product_id,
      dataType:"html",
      success:function(data)
      {
        console.log(data);
      }
	});
   }

}