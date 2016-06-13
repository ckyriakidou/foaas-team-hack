#!/usr/bin/python
# Description: This script should be part of the
# templates git directory that would use the API scripts to push and modify
# kickstart templates in satellite using the Sat 6 api.
# jenkins user should have the .hammer/cli_config.yaml file in its
# home directory that would allow for sat6 authentication.
# Takes in account production branch and other dev branches
# When a non-production branch is changed, a sat6 api call is used to
# create a new file:  branchname_filename. This would allow the separation of
# the production templates with he Development ones.
# When changes are made to the production branch they WILL overwrite the
# production templates. Use with caution.
#
# Does not download or modify locked templates


def main():
    """
    Templates need to be updated when a user changes them.
    depending on the git branch.
    """


if __name__ == "__main__":
    main()

