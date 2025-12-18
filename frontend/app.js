const OPENAI_KEY = "sk-live-REALKEY123";

fetch("https://api.openai.com/v1/chat", {
  headers: {
    Authorization: `Bearer ${OPENAI_KEY}`
  }
});
