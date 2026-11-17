import argparse
import json

from infra_glass.core.dns import get_ip_addresses


def main():
    parser = argparse.ArgumentParser(
        description="Infra Glass - Network inspection tool"
    )

    parser.add_argument(
        "domain",
        help="Domain name to inspect"
    )

    args = parser.parse_args()

    result = get_ip_addresses(args.domain)

    print(json.dumps(result, indent=4))