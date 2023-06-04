      function copyToClipboard(text) {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("copy");
        textArea.remove();
      }

      const button = document.getElementById("copy-button");
      button.addEventListener("click", () => {
        const text = document.getElementById("text-to-copy").innerText;
        copyToClipboard(text);
      });
