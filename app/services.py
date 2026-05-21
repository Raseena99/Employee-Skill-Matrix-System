REQUIRED_SKILLS = {
"Backend Team": [
"python",
"fastapi",
"sql",
"docker"
],
"AI Team": [
"python",
"machine learning",
"pandas",
"numpy"
],
"Cloud Team": [
"aws",
"docker",
"kubernetes"
]
}
def calculate_skill_gap(employee_skills, team_name):
required = REQUIRED_SKILLS.get(team_name, [])
employee_skills = [s.lower() for s in employee_skills]
missing = []
for skill in required:
if skill.lower() not in employee_skills:
missing.append(skill)
return missing
def recommend_learning(employee_skills):
recommendations = []
employee_skills = [s.lower() for s in employee_skills]
if "docker" not in employee_skills:
recommendations.append("Learn Docker")
if "aws" not in employee_skills:
recommendations.append("Learn AWS Cloud")
if "fastapi" not in employee_skills:
recommendations.append("Build REST APIs with FastAPI")
if "machine learning" not in employee_skills:
recommendations.append("Take Machine Learning Fundamentals")
return recommendations
