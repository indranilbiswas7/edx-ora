from django.contrib.auth.models import User
from django.test.client import Client

from controller.models import Submission, Grader, SubmissionState , GraderStatus

from django.utils import timezone

from controller.models import Submission,Grader
from peer_grading.models import CalibrationHistory,CalibrationRecord

def create_user():

    if(User.objects.filter(username='test').count() == 0):
        user = User.objects.create_user('test', 'test@test.com', 'CambridgeMA')
        user.save()

def delete_all():
    for sub in Submission.objects.all():
        sub.delete()

    for grade in Grader.objects.all():
        grade.delete()

    for cal_hist in CalibrationHistory.objects.all():
        cal_hist.delete()

    for cal_record in CalibrationRecord.objects.all():
        cal_record.delete()

def get_sub(grader_type,student_id,location):
    test_sub = Submission(
        prompt="prompt",
        student_id=student_id,
        problem_id="id",
        state=SubmissionState.waiting_to_be_graded,
        student_response="response",
        student_submission_time=timezone.now(),
        xqueue_submission_id="id",
        xqueue_submission_key="key",
        xqueue_queue_name="MITx-6.002x",
        location=location,
        course_id="course_id",
        max_score=3,
        next_grader_type=grader_type,
        previous_grader_type=grader_type,
    )
    return test_sub

def get_grader(grader_type):
    test_grader=Grader(
        score=0,
        feedback="",
        status_code=GraderStatus.success,
        grader_id="1",
        grader_type=grader_type,
        confidence=1,
        is_calibration=False,
    )

    return test_grader

