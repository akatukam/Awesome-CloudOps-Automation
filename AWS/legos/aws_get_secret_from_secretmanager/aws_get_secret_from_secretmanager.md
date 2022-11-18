{
"action_title": " Get secrets from secretsmanager",
"action_description": " Get secrets from AWS secretsmanager",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_get_secret_from_secretmanager",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_STR",
"action_supports_iteration": true,
"action_verbs": ["get"],
"action_nouns": [
"secrets",
"secretsmanager"
]
}