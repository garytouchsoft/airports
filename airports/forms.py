from django import forms  

class LocationForm(forms.Form):  
    latitude = forms.DecimalField(label="Enter Latitude")  
    longitude  = forms.DecimalField(label="Enter Longitude")  
    
    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if abs(latitude) > 90:
            raise forms.ValidationError("Invalid latitude")
        return latitude
        
    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if abs(longitude) > 180:
            raise forms.ValidationError("Invalid longitude")
        return longitude
