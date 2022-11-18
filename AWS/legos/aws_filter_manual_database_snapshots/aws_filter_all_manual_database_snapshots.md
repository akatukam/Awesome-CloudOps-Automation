{
"action_title": "AWS Filter All Manual Databse Snapshots",
"action_description": "Use This Action to AWS Filter All Manual Databse Snapshots",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_get_manual_database_snapshots",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_LIST",
"action_supports_iteration": true,
"action_verbs": [
"get"
],
"action_nouns": [
"rds",
"manual",
"database"
]
}