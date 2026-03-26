const API_BASE = "http://localhost:8000";

document.addEventListener('DOMContentLoaded', () => {
    // 1. View Management System
    const menuItems = document.querySelectorAll('.menu-item[data-view]');
    const views = document.querySelectorAll('.content-view');

    const switchView = (viewId) => {
        views.forEach(v => v.classList.remove('active'));
        menuItems.forEach(mi => mi.classList.remove('active'));

        const targetView = document.getElementById(`view-${viewId}`);
        const activeMenuItem = document.querySelector(`.menu-item[data-view="${viewId}"]`);

        if (targetView && activeMenuItem) {
            targetView.classList.add('active');
            activeMenuItem.classList.add('active');
            initViewContent(viewId);
        }
    };

    menuItems.forEach(item => {
        item.addEventListener('click', () => switchView(item.dataset.view));
    });

    const initViewContent = (viewId) => {
        switch(viewId) {
            case 'dashboard': loadDashboardData(); break;
            case 'dmit': loadDMITForm(); break;
            case 'roadmap': loadRoadmapForm(); break;
            case 'skills': loadSkillsData(); break;
        }
    };

    // 2. Dashboard Loading Logic
    let dmitChartObj = null;
    const loadDashboardData = async () => {
        try {
            const studentId = "student_001";
            const response = await fetch(`${API_BASE}/api/dmit/${studentId}`);
            const data = await response.json();

            // Render Radar Chart
            const ctx = document.getElementById('dmitChart').getContext('2d');
            if (dmitChartObj) dmitChartObj.destroy();
            dmitChartObj = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: Object.keys(data.traits),
                    datasets: [{
                        label: 'Dominance Profile (%)',
                        data: Object.values(data.traits),
                        backgroundColor: 'rgba(37, 99, 235, 0.2)',
                        borderColor: '#2563eb',
                        pointBackgroundColor: '#2563eb'
                    }]
                },
                options: { 
                    scales: { r: { grid: { color: 'rgba(0, 0, 0, 0.1)' }, angleLines: { color: 'rgba(0, 0, 0, 0.1)' }, pointLabels: { color: '#64748b' }, ticks: { display: false } } },
                    plugins: { legend: { display: false } }
                }
            });

            // Cognitive Progress Bars
            const cognContainer = document.getElementById('cognitiveInsights');
            cognContainer.innerHTML = '';
            const brainData = data.brain_dominance;
            for (const [key, value] of Object.entries(brainData)) {
                const label = key.replace('_', ' ').replace(/\b\w/g, c => c.toUpperCase());
                cognContainer.innerHTML += `
                    <div class="progress-container">
                        <div class="progress-label"><span>${label}</span><span>${value}%</span></div>
                        <div class="progress-bar"><div class="progress-fill" style="width: ${value}%"></div></div>
                    </div>
                `;
            }

            // Career Recommendations (Calling recommendation endpoint with mock data)
            const recResp = await fetch(`${API_BASE}/api/recommend-career`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: "Aryan Sharma", age: 18, aptitude_score: 85, interest_score: 80,
                    dmit_traits: data.traits, academic_background: 90
                })
            });
            const recData = await recResp.json();
            const recList = document.getElementById('careerRecommendationList');
            recList.innerHTML = '';
            recData.recommendations.forEach(rec => {
                recList.innerHTML += `
                    <div class="career-item glass animate-fade-in stagger-1">
                        <div>
                            <strong>${rec.career}</strong>
                            <p style="font-size: 0.8rem; color: var(--text-dim); margin-top: 5px;">${rec.reasoning}</p>
                        </div>
                        <div style="text-align: right;">
                            <span class="gradient-text" style="font-size: 1.2rem; font-weight: 800;">${(rec.score * 100).toFixed(0)}% Match</span>
                            <br/><i class="fas fa-chevron-right" style="color: var(--text-dim); font-size: 0.7rem; margin-top: 5px;"></i>
                        </div>
                    </div>
                `;
            });

        } catch (err) { console.error("Dashboard Load Error:", err); }
    };

    // 3. DMIT Questionnaire
    const loadDMITForm = () => {
        const form = document.getElementById('dmitForm');
        form.innerHTML = `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div class="glass" style="padding: 15px;">
                    <label>Aptitude Score</label>
                    <input type="range" class="form-slider" min="0" max="100" value="80" style="width: 100%; margin-top: 10px;">
                </div>
                <!-- Extend with more sliders/inputs as needed -->
            </div>
            <button class="send-btn" style="width: 100%; border-radius: 12px; margin-top: 20px;">Analyze My Traits</button>
        `;
    };

    // 4. Roadmap Logic
    const loadRoadmapForm = () => {
        const generateBtn = document.getElementById('generateRoadmapBtn');
        const roadmapInput = document.getElementById('roadmapSearch');
        const resultContainer = document.getElementById('roadmapResult');

        generateBtn.onclick = async () => {
            const query = roadmapInput.value.trim() || "Data Science";
            resultContainer.innerHTML = `<p style="color: var(--primary);">Predicting your future path...</p>`;
            try {
                const response = await fetch(`${API_BASE}/api/roadmap/${query}`);
                const data = await response.json();
                
                resultContainer.innerHTML = `<h3 style="margin-bottom: 20px;">The Life Vault <span class="gradient-text">${data.career}</span> Roadmap</h3>`;
                data.roadmap.forEach((step, idx) => {
                    resultContainer.innerHTML += `
                        <div class="glass animate-fade-in" style="padding: 20px; margin-bottom: 15px; border-left: 4px solid var(--primary);">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                <h4 style="color: var(--primary);">${step.stage}</h4>
                                <span style="font-size: 0.8rem; background: rgba(0,243,255,0.1); padding: 4px 10px; border-radius: 20px;">${step.duration}</span>
                            </div>
                            <p style="font-size: 0.95rem; margin-top: 10px; color: var(--text-main);">${step.description}</p>
                            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px;">
                                ${step.skills.map(skill => `<span style="font-size: 0.75rem; color: var(--primary); background: #eff6ff; padding: 4px 10px; border-radius: 6px; font-weight: 500;"># ${skill}</span>`).join('')}
                            </div>
                        </div>
                    `;
                });
            } catch (err) { resultContainer.innerHTML = `<p style="color: coral;">Failed to generate roadmap. Please try again.</p>`; }
        };
    };

    // 5. Skills Analytics Logic
    const loadSkillsData = async () => {
        try {
            const schoolResp = await fetch(`${API_BASE}/api/school-analytics/ST_99`);
            const corporateResp = await fetch(`${API_BASE}/api/corporate-analytics/CORP_55`);
            const sData = await schoolResp.json();
            const cData = await corporateResp.json();

            // Render School Chart
            new Chart(document.getElementById('schoolChart').getContext('2d'), {
                type: 'bar',
                data: {
                    labels: Object.keys(sData.class_wise_metrics),
                    datasets: [{
                        label: 'Average AptitudeScore',
                        data: Object.values(sData.class_wise_metrics).map(m => m.avg_aptitude),
                        backgroundColor: 'rgba(37, 99, 235, 0.6)'
                    }]
                },
                options: { scales: { y: { beginAtZero: true, grid: { color: 'rgba(0, 0, 0, 0.05)' } }, x: { grid: { display: false } } } }
            });

            // Render Corporate Gap Chart
            new Chart(document.getElementById('corporateChart').getContext('2d'), {
                type: 'bar',
                data: {
                    labels: Object.keys(cData.skill_gaps),
                    datasets: [{
                        label: 'Skill Gap Percentage (%)',
                        data: Object.values(cData.skill_gaps),
                        backgroundColor: 'rgba(79, 70, 229, 0.6)'
                    }]
                },
                options: { indexAxis: 'y', scales: { x: { grid: { color: 'rgba(0, 0, 0, 0.05)' } }, y: { grid: { display: false } } } }
            });

        } catch (err) { console.error("Skills Load Error:", err); }
    };

    // 6. AI Chat Enhancement
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');

    const addMessage = (text, type = 'ai') => {
        const bubble = document.createElement('div');
        bubble.className = `chat-bubble ${type}`;
        bubble.textContent = text;
        chatMessages.appendChild(bubble);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    const handleSend = async () => {
        const msg = userInput.value.trim();
        if (!msg) return;
        addMessage(msg, 'user');
        userInput.value = '';

        const typingId = 'typing-' + Date.now();
        const typingBubble = document.createElement('div');
        typingBubble.className = 'chat-bubble ai';
        typingBubble.id = typingId;
        typingBubble.textContent = '...Life Vault is thinking';
        chatMessages.appendChild(typingBubble);

        try {
            const response = await fetch(`${API_BASE}/api/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_message: msg }) 
            });
            const data = await response.json();
            setTimeout(() => {
                document.getElementById(typingId).remove();
                addMessage(data.response);
            }, 800);
        } catch (error) {
            document.getElementById(typingId).remove();
            addMessage("I'm momentarily disconnected from the core. Let's try again.", 'ai');
        }
    };
    sendBtn.onclick = handleSend;
    userInput.onkeypress = (e) => (e.key === 'Enter') && handleSend();

    // Initial Dashboard Load
    loadDashboardData();
});
