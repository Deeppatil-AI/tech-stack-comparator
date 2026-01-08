def compare_stacks(project_size, team_python, need_fast_api):
    mern_score = 0
    django_score = 0
    reasons = []

    if project_size == "large":
        django_score += 2
        reasons.append("Django handles large projects well.")
    else:
        mern_score += 2
        reasons.append("MERN is faster for small projects.")

    if team_python:
        django_score += 2
        reasons.append("Python experience favors Django.")
    else:
        mern_score += 2
        reasons.append("Single-language JS stack favors MERN.")

    if need_fast_api:
        django_score += 1
        reasons.append("Django REST is robust.")
    else:
        mern_score += 1
        reasons.append("Node APIs are lightweight.")

    print("\nRecommended Stack:")
    print("Django + React" if django_score > mern_score else "MERN Stack")

    print("\nTrade-offs:")
    for r in reasons:
        print("-", r)


compare_stacks("large", True, True)
