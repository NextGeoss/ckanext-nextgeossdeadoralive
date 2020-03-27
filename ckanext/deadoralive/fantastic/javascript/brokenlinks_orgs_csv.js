function download_orgs_csv(broken_links_array){//Function to create CSV_File and download from broken links webpage
    check_resource = document.getElementsByTagName('input');
    var data_for_csv=[];
    var csvContent = "data:text/csv;charset=utf-8,";
    for (i=0; i < check_resource.length; i++){		//Resources for csv
        if(check_resource[i].type == 'checkbox'){
          if(check_resource[i].checked)
           data_for_csv.push(check_resource[i].value);
        }
    }

    //Adding static url for the urls in broken_links_array
    var static_url = "http://127.0.0.1:5000";
    broken_links_array.forEach(function(rowArray){      
       rowArray[1] = static_url + rowArray[1];
       rowArray[3] = static_url + rowArray[3];
       rowArray[5] = static_url + rowArray[5];
    });
    
    //Creating CSV
    csvContent += "ORGANIZATION,URL_ORGANIZATION,DATASET,URL_DATASET,RESOURCE,URL_RESOURCE\r\n"//First row for variable for each column (Table Head)
    broken_links_array.forEach(function(rowArray){      
       var row = "";
       if(data_for_csv.includes(rowArray[4])){
          row = rowArray.join(",");
          csvContent += row + "\r\n";
       }
    });

    //Creating a child in the webpage to force download and to add and specified name
    var encodedUri = encodeURI(csvContent);
    var link_download = document.createElement("a");
    var date = new Date();
    var month = date.getMonth() + 1 ;
    var file_name = "csv_broken_links_org_" + date.getFullYear().toString() + month.toString() + date.getDate().toString() + "_" + date.getHours().toString() + date.getMinutes().toString()  + date.getSeconds().toString() + ".csv";
    link_download.setAttribute("href",encodedUri);
    link_download.setAttribute("download",file_name);
    document.body.appendChild(link_download);//Added new child in body for specified name
    link_download.click();
    document.body.removeChild(link_download);//Removing
}

//--------------------------------------------------------------------------------------------------------------

function download_user_csv(broken_links_array){//Function to create CSV_File and download from user (ckan-admin)
    check_resource = document.getElementsByClassName("chk_resource");
    var data_for_csv=[];
    var csvContent = "data:text/csv;charset=utf-8,";
    for (i=0; i < check_resource.length; i++){		//Resources for csv
        if(check_resource[i].checked)
           data_for_csv.push(check_resource[i].value);
    }

    //Adding static url for the urls in broken_links_array
    var static_url = "http://127.0.0.1:5000";
    broken_links_array.forEach(function(rowArray){
       rowArray[3] = static_url + rowArray[3];
       rowArray[5] = static_url + rowArray[5];
    });
    
    //Creating CSV
    csvContent += "EMAIL_USER,MAILTO_MANTAINER,DATASET,URL_DATASET,RESOURCE,URL_RESOURCE\r\n"//First row for variable for each column (Table Head)
    broken_links_array.forEach(function(rowArray){      
       var row = "";
       if(data_for_csv.includes(rowArray[4])){
          row = rowArray.join(",");
          csvContent += row + "\r\n";
       }
    });

    //Creating a child in the webpage to force download and to add and specified name
    var encodedUri = encodeURI(csvContent);
    var link_download = document.createElement("a");
    var date = new Date();
    var month = date.getMonth() + 1 ;
    var file_name = "csv_broken_links_user_" + date.getFullYear().toString() + month.toString() + date.getDate().toString() + "_" + date.getHours().toString() + date.getMinutes().toString()  + date.getSeconds().toString() + ".csv";
    link_download.setAttribute("href",encodedUri);
    link_download.setAttribute("download",file_name);
    document.body.appendChild(link_download);//Added new child in body for specified name
    link_download.click();
    document.body.removeChild(link_download);//Removing
}

//-------------------------------------------------------------------

function select_all(){//Function to select all checkboxes
    check_resource = document.getElementsByClassName("chk_resource");
    for (i=0; i < check_resource.length; i++){
        check_resource[i].checked = 1;
    }
}

//-------------------------------------------------------------------

function clean_selection(){//Function to clean the selection
    check_resource = document.getElementsByClassName("chk_resource");
    for (i=0; i < check_resource.length; i++){
        check_resource[i].checked = 0;
    }
    
}

//-------------------------------------------------------------------

function select_org(id){//Function to select all resources from any org by Id
    check_resource = document.getElementById(id).getElementsByTagName('input');
    for (i=0; i < check_resource.length; i++){
        if(check_resource[i].type == 'checkbox'){
          check_resource[i].checked = 1;
        }
    }
}

//------------------------------------------------------------------

function clean_org(id){//Function to clean all resources from any org by Id
    check_resource = document.getElementById(id).getElementsByTagName('input');
    for (i=0; i < check_resource.length; i++){
        if(check_resource[i].type == 'checkbox'){
          check_resource[i].checked = 0;
        }
    }
}
