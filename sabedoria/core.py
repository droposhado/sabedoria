
import requests


def convert(total_minutes):
    """convert minutes to hours"""

    total_minutes = int(total_minutes)
    # Get hours with floor division
    hours = total_minutes // 60

    # Get additional minutes with modulus
    # minutes = total_minutes % 60

    # Create time as a string
    # if minutes != 0:
    #    time = float("{}.{}".format(hours, minutes))
    # else:
    #    time = float("{}.0".format(hours))

    return hours


def get_table(base_url, token, table_id, params):
    """Function to get data from baserow api"""

    req = requests.get(
        f"{base_url}/api/database/rows/table/{table_id}/",
        headers={
            "Authorization": f"Token {token}"
        }, params=params, timeout=5)

    return req.json().get("results")


def get_socials(cfg):
    """Get socials from env variables"""

    socials = {
        "github": cfg["GITHUB"],
        "linkedin": cfg["LINKEDIN"],
        "email": cfg["EMAIL"],
        "site": cfg["SITE"]
    }
    return socials


def get_descriptions(base_url, token, descs_table_id, lang):
    """Get descriptions from baserow"""

    params = {
        "user_field_names":True
    }

    descs_table = get_table(base_url, token, descs_table_id, params)
    if descs_table is None:
        return []

    descs = []
    for result in descs_table:
        descs.append({
            "scope": result["scope"],
            "value": result[lang]
        })

    return descs


def get_courses(base_url, token, courses_table_id):
    """Get courses list from baserow table"""

    params = {
        "user_field_names": True,

        # status done
        "filter__field_834257__single_select_equal": 382593,

        # public true
        "filter__field_836592__boolean": True,

        "order_by": "name"
    }

    courses_table = get_table(base_url, token, courses_table_id, params)
    if courses_table is None:
        return []

    courses = []
    for result in courses_table:
        courses.append({
            "name": result["name"],
            "certificate_url": result["certificate_url"],
            "course_url": result["url"],
            "organization_name": result["platform"]["value"],
            "end": result["completed"],
            "hours": convert(result["minutes"]),
            "minutes": int(result["minutes"])
        })

    return courses


def get_jobs(base_url, token, jobs_table_id, lang):
    """Get jobs list from baserow table"""

    params = {
        "user_field_names": True,
        "order_by": "-end"
    }

    jobs_table = get_table(base_url, token, jobs_table_id, params)
    if jobs_table is None:
        return []

    jobs = []
    for result in jobs_table:
        jobs.append({
            "contract_type": result["contract_type"]["value"],
            "description": [d["value"] for d in result["description_" + lang]],
            "employer": result["employer"],
            "end": result["end"],
            "location": result["location"],
            "location_type": result["location_type"]["value"],
            "skill": [s["value"] for s in result["skill"]],
            "start": result["start"],
            "title": result["title_" + lang],
        })

    return jobs


def get_projects(base_url, token, projects_table_id, lang):
    """Get projects list from baserow table"""

    params = {
        "user_field_names": True,

        # id for show field
        "filter__field_987837__boolean": True,

        "order_by": "name"
    }

    projects_table = get_table(base_url, token, projects_table_id, params)
    if projects_table is None:
        return []

    projects = []
    for result in projects_table:
        projects.append({
            "description": result["description_" + lang],
            "name": result["name"],
            "skill": [s["value"] for s in result["skill"]],
            "stage": result["stage"]["value"],
            "url": result["url"],
            "visibility": result["visibility"]["value"]
        })

    return projects


def get_educations(base_url, token, educations_table_id, lang):
    """Get educationss list from baserow table"""

    params = {
        "user_field_names": True,
        "order_by": "-end"
    }

    educations_table = get_table(base_url, token, educations_table_id, params)
    if educations_table is None:
        return []

    educations = []
    for result in educations_table:
        educations.append({
            "university": result["university"],
            "start": result["start"],
            "end": result["end"],
            "thesis": result["thesis_" + lang],
            "location": result["location"],
            "title": result["title_" + lang]
        })

    return educations


def get_interests(base_url, token, interests_table_id, lang):
    """Get interests list from baserow table"""

    params = {
        "user_field_names": True
    }

    interests_table = get_table(base_url, token, interests_table_id, params)
    if interests_table is None:
        return []

    interests = []
    for result in interests_table:
        interests.append(result[lang])

    return interests
