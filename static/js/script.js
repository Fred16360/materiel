function popup(page, titre, largeur, hauteur, options) {
    if (options == null) {
        options = 'resizable=no, location=no, status=no, scrollbars=no, menubar=no, toolbar=no';
    }
    // document.body.style.backgroundColor = "#000";
    // document.body.style.opacity = "0.4";
    var top = (screen.height - hauteur) / 2 - 30;
    var left = (screen.width - largeur) / 2;
    var w = window.open(page, titre, `top=${top},left=${left},width=${largeur},height=${hauteur},${options}`);
    w.focus();

}

  
function capitalize(string)  {
	  return string[0].toUpperCase() + string.slice(1);
}


function display_mdp(password) {
	document.getElementById('password').innerHTML = password;
	document.getElementById('mdp_view').style.display = "block";
}


function open_view(id, title) {
	document.getElementById(id).style.display = "block";
}


function close_view(id) {
	document.getElementById(id).style.display = "none";
}


/*
function insertSupplier() {
	var agency = {
		supplier_id : 0,
		address : document.getElementById("form_agency_address").value,
		zipcode : document.getElementById("form_agency_zipcode").value,
		city :  document.getElementById("form_agency_city").value,
		supplier_keyword :  document.getElementById("form_agency_keyword").value,
		gps_location :  document.getElementById("form_agency_gps_location").value,
		phone :  document.getElementById("form_agency_phone").value,
		email :  document.getElementById("form_agency_email").value	};
	var supplier = {
		name : document.getElementById("form_supplier_name").value
	};

	var xhr = getXMLHttpRequest();
	xhr.onreadystatechange = function() {
		if( xhr.readyState == 4) {
			if( xhr.status == 200 ) {
				response = JSON.parse(xhr.responseText.trim());
				searchSuppliers();
				getSupplier(response.supplier_id, response.agency_id);
				document.getElementById('form_supplier_window').style.display = "none";
			} else {
				console.log("insertSupplier - Le serveur ne repond pas...");
			}
		}    
	};

	xhr.open("POST", site_url + "/supply/supplier/ajxInsertSupplier/", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xhr.send("supplier="+JSON.stringify(supplier)+"&agency="+JSON.stringify(agency));
}

class Agency {
	constructor(json_agency) {
		this.agency_id = json_agency.agency_id;
		
		this.keyword = json_agency.keyword;
		this.address = json_agency.address;
		this.zipcode = json_agency.zipcode;
		this.city = json_agency.city;
		this.gps_location = json_agency.gps_location;
		this.phone = json_agency.phone;
		this.email = json_agency.email;

		this.distance = -1;
		if(this.gps_location != "" && dossier_gps_location != "") {
			this.distance = calcDistanceWithLatitudeAndLongitude(this.gps_location, dossier_gps_location);
		}

		this.contacts = [];
		for(var key in json_agency.contacts) {
			this.contacts.push(new Contact(json_agency.contacts[key]));
		}
	}

	getAddress() {
		return this.address;
	}

	getZipcodeCity() {
		return this.zipcode + " " + this.city;
	}
}
*/