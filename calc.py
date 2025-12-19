def get_failure_probability(
    participants, total_meeting_slots, rejections_per_participant
):
    if rejections_per_participant >= total_meeting_slots:
        return 0.0  # all meeting slots rejected
    if participants * rejections_per_participant < total_meeting_slots:
        return 1.0  # not enough rejects to block all meeting slots

    probability_of_acceptance_per_slot = (
        total_meeting_slots - rejections_per_participant
    ) / total_meeting_slots
    probability_no_slots_accepted = (
        1 - probability_of_acceptance_per_slot**participants
    ) ** total_meeting_slots
    return probability_no_slots_accepted


def get_success_probability(
    participants, total_meeting_slots, rejections_per_participant
):
    # complement of no slots accepted. prob at least one slot works
    return 1 - get_failure_probability(
        participants, total_meeting_slots, rejections_per_participant
    )
