  $('.checkbox').change(function(){
    var val=$(this).is(":checked")
    var s_uid = $(this).attr("id");
    vall = s_uid.split(/(\d+)/)
    num = vall[1]
    nam = vall[0]

    console.log(nam);
    console.log(val);

if (nam=="editor" && val == true)
{
          $("#viewer"+num+"").prop('checked', true);
}
if (nam=="viewer" && val == false)
{
          $("#editor"+num).prop('checked', false);
}
});

