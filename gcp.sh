curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init

gcloud auth activate-service-account --key-file=YOUR_KEY_FILE.json
