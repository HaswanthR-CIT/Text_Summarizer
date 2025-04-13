document.addEventListener('DOMContentLoaded', () => {
    const tags = document.querySelectorAll('.topic-tag');
    const originalText = document.querySelector('#original-text');

    tags.forEach(tag => {
        tag.addEventListener('click', () => {
            const topic = tag.getAttribute('data-topic');
            const text = originalText.textContent;
            originalText.innerHTML = text;

            const regex = new RegExp(`\\b${topic}\\b`, 'gi');
            originalText.innerHTML = text.replace(regex, `<span class="highlight">${topic}</span>`);

            // Add subtle pulse
            tags.forEach(t => t.classList.remove('pulse'));
            tag.classList.add('pulse');
        });
    });
});