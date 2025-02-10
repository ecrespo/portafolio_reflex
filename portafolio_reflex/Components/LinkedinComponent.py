import reflex as rx




def Linkedin(fullname:str)-> rx.Component:
    return rx.html(f"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="{fullname}" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ernestocrespo/?trk=profile-badge&originalSubdomain=in"></a></div>""")