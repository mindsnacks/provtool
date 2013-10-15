Installation
------------

This should work:

    (sudo) pip install provtool

Features
--------

usage: `provtool <subcommand>`

Available subcommands are:

 * `list`            - List installed Provisining Profiles.
 * `path <name>`     - Get the path(s) of Provisioning Profile by name.
 * `uuid <path>`     - Display the UDID of a Provisioning Profile by path.


Examples
--------

	$ provtool list
	EBB1133B-C2A2-4A8F-ADE6-E7930E2DED49.mobileprovision : 'MyApp Ad Hoc'
	FA13FEF3-6286-4F70-B820-F89C3C030D8A.mobileprovision : 'MyApp App Store'

	$ provtool path "MyApp App Store"
	/Users/me/Library/MobileDevice/Provisioning Profiles/FA13FEF3-6286-4F70-B820-F89C3C030D8A.mobileprovision

	$ provtool uuid "/Users/me/Library/MobileDevice/Provisioning Profiles/FA13FEF3-6286-4F70-B820-F89C3C030D8A.mobileprovision"
	FA13FEF3-6286-4F70-B820-F89C3C030D8A

	$ provtool uuid "$(provtool path 'MyApp App Store')" 
	FA13FEF3-6286-4F70-B820-F89C3C030D8A
