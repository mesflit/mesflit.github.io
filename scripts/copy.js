document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("pre > code").forEach(function (codeBlock) {
        const button = document.createElement("button");
        button.innerText = "Kopyala";
        button.style.float = "right";
        button.style.marginBottom = "5px";

        button.addEventListener("click", function () {
            const text = codeBlock.innerText;
            navigator.clipboard.writeText(text).then(function () {
                button.innerText = "Kopyalandı!";
                setTimeout(() => (button.innerText = "Kopyala"), 2000);
            });
        });

        const pre = codeBlock.parentNode;
        pre.parentNode.insertBefore(button, pre);
    });
});
