# Batch Transcription

This repo contains a handful of simple functions to interact with the Batch Transcription API exposed by Azure Speech Services.

## Prerequisites

* An Azure account
* A Speech Services S0 subscription
* An Azure Blob Storage account to store your audio files
* Python 3.6 or later

## What's in this repo?

There are four functions in this repo:

* `transcribe.py` - Transcribe a single file from Azure Blob Storage.
* `get_transcription.py` - Get a full list of transcription requests associated with your subscription and the status for each.
* `delete_transcriptions.py` - Delete a single transcription.
* `delete_all.py` - Delete all transcriptions associated with your subscription.
