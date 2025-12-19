from calc import get_failure_probability, get_success_probability
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Meeting probability calculator",
        epilog="Example: python3 main.py 5 40 20",
    )
    parser.add_argument("participants", type=int, help="Number of meeting participants")
    parser.add_argument(
        "total_meeting_slots",
        type=int,
        help="Total number of available meeting time slots",
    )
    parser.add_argument(
        "rejections", type=int, help="Number of slots each participant rejects"
    )
    args = parser.parse_args()

    if args.participants < 1:
        parser.error("Need at least 1 participant")
    if args.total_meeting_slots < 1:
        parser.error("Need at least 1 meeting time slot")

    success_prob = get_success_probability(
        args.participants, args.total_meeting_slots, args.rejections
    )
    failure_prob = get_failure_probability(
        args.participants, args.total_meeting_slots, args.rejections
    )

    print(f"Success probability: {success_prob:.2%}")
    print(f"Failure probability: {failure_prob:.2%}")


if __name__ == "__main__":
    main()
