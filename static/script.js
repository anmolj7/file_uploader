//Credits for this code: https://stackoverflow.com/a/45347868
var valid = false;
var fileName = false;

function validate_fileupload(input_element)
{
    var el = document.getElementById("feedback");
    fileName = input_element.value;
    var allowed_extensions = new Array("txt","md");
    var file_extension = fileName.split('.').pop();
    for(var i = 0; i < allowed_extensions.length; i++)
    {
        if(allowed_extensions[i]==file_extension)
        {
            valid = true; // valid file extension
            el.innerHTML = "";
            return;
        }
    }
    el.innerHTML="Invalid file";
    valid = false;
}

function valid_form()
{
    if(!valid){
        if(!fileName){
            alert("Select A File!");
        }
        else
            alert("Only .txt and .md files are allowed!");
    }
    return valid;
}

