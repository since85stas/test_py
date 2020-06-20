from collections import defaultdict

import unicodecsv as unicodecsv
import numpy as np

from datetime import datetime as dt

def parse_date(date):
    if (date == ''):
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def pare_int(num):
    if (num == ''):
        return None
    else:
        return int(num)


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

enrollSet = set()
dailySet = set()
projSet = set()
# ----------------------------------------------------------------------------
for item in enrollments:
    item['join_date'] = parse_date(item['join_date'])
    item['cancel_date'] = parse_date(item['cancel_date'])
    item['days_to_cancel'] = pare_int(item['days_to_cancel'])
    item['is_udacity'] = item['is_udacity'] == 'True'
    item['is_canceled'] = item['is_canceled'] == 'True'
    enrollSet.add(item['account_key'])

for item in daily_engagement:
    item['utc_date'] = parse_date(item['utc_date'])
    item['num_courses_visited'] = int(float(item['num_courses_visited']))
    item['total_minutes_visited'] = int(float(item['total_minutes_visited']))
    item['lessons_completed'] = int(float(item['lessons_completed']))
    item['projects_completed'] = int(float(item['projects_completed']))
    dailySet.add(item['acct'])

for item in project_submissions:
    item['creation_date'] = parse_date(item['creation_date'])
    item['completion_date'] = parse_date(item['completion_date'])
    projSet.add(item['account_key'])
#-----------------------------------------------------------------------------------------------

for item in daily_engagement:
    item['account_key'] = item['acct']
    del(item['acct'])

num_problems = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in dailySet \
            and enrollment['join_date'] != enrollment['cancel_date']:
        print(enrollment)
        num_problems += 1
        break

# --------------------------------------------------------------------------------------------------------------
udacity_test_accounts = set()
for enrollment in enrollments:
    if (enrollment['is_udacity'] == True):
        udacity_test_accounts.add(enrollment['account_key'])

def remove_tests(data_set):
    non_udac_data = []
    for data in data_set:
        if (data['account_key'] not in udacity_test_accounts):
            non_udac_data.append(data)
    return non_udac_data

non_udacity_enrollments = remove_tests(enrollments)
non_udacity_engagement = remove_tests(daily_engagement)
non_udacity_submissions = remove_tests(project_submissions)
#---------------------------------------------------------------------------------------------------------------
enrollment_num_rows = len(non_udacity_enrollments)  # Replace this with your code
engagement_num_rows = len(non_udacity_engagement)             # Replace this with your code
submission_num_rows = len(non_udacity_submissions)             # Replace this with your code
#---------------------------------------------------------------------------------------------------------------
paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
len(paid_students)
# ------------------------------------------------------------------------------------------------------
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print (len(paid_enrollments))
print (len(paid_engagement))
print (len(paid_submissions))

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
         paid_engagement_in_first_week.append(engagement_record)

len(paid_engagement_in_first_week)
# -----------------------------------------------------------------------------------------------------------
engagement_by_account = defaultdict(list)
for engage in paid_engagement_in_first_week:
    account_key = engage['account_key']
    engagement_by_account[account_key].append(engage)

total_minutes_by_account = {}
for account, engage in engagement_by_account.items():
    total_minutes = 0
    for items in engage:
        total_minutes += items['total_minutes_visited']
    total_minutes_by_account[account] = total_minutes

minutes_list = sorted(total_minutes_by_account.values(), reverse= True)
# ------------------------------------------------------------------------------------------------------------
student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student

max_minutes

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print (engagement_record)

# max(total_minutes_by_account.items(), key=lambda pair: pair[1])
#---------------------------------------------------------------------------------------------------------------
def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

engagement_by_account = group_data(paid_engagement_in_first_week,
                                   'account_key')

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

total_minutes_by_account = sum_grouped_items(engagement_by_account,
                                             'total_minutes_visited')

def describe_data(data):
    print ('Mean:', np.mean(data))
    print ('Standard deviation:', np.std(data))
    print ('Minimum:', np.min(data))
    print ('Maximum:', np.max(data))

describe_data(total_minutes_by_account.values())

# ---------------------------------------------------------------------------------------------
print("end")


