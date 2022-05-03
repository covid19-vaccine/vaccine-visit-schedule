from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import esr21_enrollment_schedule, esr21_fu_schedule
from .schedules import esr21_sub_enrollment_schedule, esr21_sub_fu_schedule
from .schedules import esr21_illness_schedule, esr21_illness2_schedule
from .schedules import esr21_illness3_schedule, esr21_illness4_schedule
from .schedules import esr21_illness5_schedule, esr21_illness6_schedule
from .schedules import esr21_illness7_schedule, esr21_illness8_schedule
from .schedules import esr21_illness9_schedule, esr21_illness10_schedule
from .schedules import esr21_illness11_schedule, esr21_illness12_schedule
from .schedules import esr21_enrol_schedule_v3, esr21_fu_schedule_v3
from .schedules import esr21_booster_schedule, esr21_sub_enrol_schedule3
from .schedules import esr21_sub_fu_schedule3, esr21_sub_boost_schedule

esr21_visit_schedule = VisitSchedule(
    name='esr21_visit_schedule',
    verbose_name='ESR21',
    offstudy_model='esr21_prn.subjectoffstudy',
    locator_model='esr21_subject.personalcontactinfo',
    death_report_model='esr21_prn.deathreport',
    previous_visit_schedule=None)

esr21_visit_schedule.add_schedule(esr21_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_fu_schedule)

esr21_visit_schedule.add_schedule(esr21_sub_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_sub_fu_schedule)

esr21_visit_schedule.add_schedule(esr21_enrol_schedule_v3)
esr21_visit_schedule.add_schedule(esr21_fu_schedule_v3)
esr21_visit_schedule.add_schedule(esr21_booster_schedule)

esr21_visit_schedule.add_schedule(esr21_sub_enrol_schedule3)
esr21_visit_schedule.add_schedule(esr21_sub_fu_schedule3)
esr21_visit_schedule.add_schedule(esr21_sub_boost_schedule)

esr21_visit_schedule.add_schedule(esr21_illness_schedule)
esr21_visit_schedule.add_schedule(esr21_illness2_schedule)
esr21_visit_schedule.add_schedule(esr21_illness3_schedule)
esr21_visit_schedule.add_schedule(esr21_illness4_schedule)
esr21_visit_schedule.add_schedule(esr21_illness5_schedule)
esr21_visit_schedule.add_schedule(esr21_illness6_schedule)
esr21_visit_schedule.add_schedule(esr21_illness7_schedule)
esr21_visit_schedule.add_schedule(esr21_illness8_schedule)
esr21_visit_schedule.add_schedule(esr21_illness9_schedule)
esr21_visit_schedule.add_schedule(esr21_illness10_schedule)
esr21_visit_schedule.add_schedule(esr21_illness11_schedule)
esr21_visit_schedule.add_schedule(esr21_illness12_schedule)

site_visit_schedules.register(esr21_visit_schedule)
