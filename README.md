

- **📋 Email Categorization**: Automatically categorizes emails into specific types (newsletters, promotions, personal, etc.)
- **🔔 Priority Assignment**: Assigns priority levels (HIGH, MEDIUM, LOW) based on content and sender with strict classification rules
- **🏷️ Smart Organization**: Applies Gmail labels and stars based on categories and priorities
- **💬 Automated Responses**: Generates draft responses for important emails that need replies
- **📱 Slack Notifications**: Sends creative notifications for high-priority emails
- **🧹 Intelligent Cleanup**: Safely deletes low-priority emails based on age and category
- **🎬 YouTube Content Protection**: Special handling for YouTube-related emails
- **🗑️ Trash Management**: Automatically empties trash to free up storage space
- **🧵 Thread Awareness**: Recognizes and properly handles email threads

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click **Create New App**
3. Select **From scratch**
4. Enter `Gmail Notifications` as the app name
5. Select your workspace and click **Create App**
6. In the left sidebar, find and click on **Incoming Webhooks**
7. Toggle the switch to **Activate Incoming Webhooks**
8. Click **Add New Webhook to Workspace**
9. Select the channel where you want to receive notifications
10. Click **Allow**
11. Find the **Webhook URL** section and copy the URL that begins with `https://hooks.slack.com/services/`
12. Paste this URL in your `.env` file as the `SLACK_WEBHOOK_URL` value

**Customizing your Slack app (optional):**
1. Go to **Basic Information** in the left sidebar
2. Scroll down to **Display Information**
3. Add an app icon and description
4. Click **Save Changes**

**Note**: You need admin permissions or the ability to install apps in your Slack workspace.
</details>

## 📧 How It Works

This application uses the IMAP (Internet Message Access Protocol) to securely connect to your Gmail account and manage your emails. Here's how it works:

<details>
<summary><b>🔄 IMAP Connection Process</b></summary>

1. **Secure Connection**: The application establishes a secure SSL connection to Gmail's IMAP server (`imap.gmail.com`).

2. **Authentication**: It authenticates using your email address and app password (not your regular Google password).

3. **Mailbox Access**: Once authenticated, it can access your inbox and other mailboxes to:
   - Read unread emails
   - Apply labels
   - Move emails to trash
   - Save draft responses

4. **Safe Disconnection**: After each operation, the connection is properly closed to maintain security.

IMAP allows the application to work with your emails while they remain on Google's servers, unlike POP3 which would download them to your device. This means you can still access all emails through the regular Gmail interface.

**Security Note**: Your credentials are only stored locally in your `.env` file and are never shared with any external services.
</details>

## 🔍 Usage

Run the application with:

```bash
crewai run
```

You'll be prompted to enter the number of emails to process (default is 5).

The application will:
1. 📥 Fetch your unread emails
2. 🔎 Categorize them by type and priority
3. ⭐ Apply appropriate labels and stars
4. ✏️ Generate draft responses for important emails
5. 🔔 Send Slack notifications for high-priority items
6. 🗑️ Clean up low-priority emails based on age
7. 🧹 Empty the trash to free up storage space


## 🌟 Special Features

- **📅 Smart Deletion Rules**: 
  - Promotions older than 2 days are automatically deleted
  - Newsletters older than 7 days (unless HIGH priority) are deleted
  - Shutterfly emails are always deleted regardless of age
  - Receipts and important documents are archived instead of deleted

- **🎬 YouTube Protection**: All YouTube-related emails are preserved and marked as READ_ONLY (you'll respond directly on YouTube)

- **✍️ Smart Response Generation**: Responses are tailored to the email context and include proper formatting

- **💡 Creative Slack Notifications**: Fun, attention-grabbing notifications for important emails

- **🧵 Thread Handling**: Properly tracks and manages email threads to maintain conversation context

## 👥 Contributing

Contributions are welcome! Please feel free to submit a [Pull Request](https://github.com/tonykipkemboi/crewai-gmail-automation/pulls).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 References

- [CrewAI](https://github.com/crewAIInc/crewAI/)
- [IMAP Protocol for Gmail](https://support.google.com/mail/answer/7126229)
- [Slack API](https://api.slack.com/messaging/webhooks)
- [Ollama](https://ollama.com/library)
- [Gemini](https://ai.google.com/gemini-api)
- [OpenAI](https://openai.com/api/)

