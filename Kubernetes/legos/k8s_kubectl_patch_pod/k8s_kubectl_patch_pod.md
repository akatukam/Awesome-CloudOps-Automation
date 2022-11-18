{
"action_title": "Kubectl update field",
"action_description": "Kubectl update field of a resource using strategic merge patch",
"action_type": "LEGO_TYPE_K8S",
"action_entry_function": "k8s_kubectl_patch_pod",
"action_needs_credential": true,
"action_supports_poll": true,
"action_supports_iteration": true,
"action_output_type": "ACTION_OUTPUT_TYPE_STR",
"action_verbs": [
"update"
],
"action_nouns": [
"field", 
"patch" 
]
}