document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analysis-form');
    const analyzeBtn = document.getElementById('btn-analyze');
    const loadingState = document.getElementById('loading-state');
    const resultsContainer = document.getElementById('results-container');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // UI Loading State
        analyzeBtn.disabled = true;
        const originalBtnContent = analyzeBtn.innerHTML;
        analyzeBtn.innerHTML = '<svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Processing...';
        
        resultsContainer.classList.add('hidden');
        loadingState.classList.remove('hidden');

        try {
            // Gather input data from the exact forms
            const requestData = {
                crack_type: document.getElementById('in-crack-type').value,
                defect: document.getElementById('in-defect').value,
                severity: document.getElementById('in-severity').value,
                location: document.getElementById('in-location').value,
                
                helmet_compliance: parseFloat(document.getElementById('in-helmet').value),
                vest_compliance: parseFloat(document.getElementById('in-vest').value),
                expected_progress: parseFloat(document.getElementById('in-expected').value),
                actual_progress: parseFloat(document.getElementById('in-actual').value),
                utilization: parseFloat(document.getElementById('in-utilization').value),
                delay_risk: document.getElementById('in-delay').value
            };

            // Fetch from local backend
            const response = await fetch('http://127.0.0.1:8000/api/analyze-maintenance', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });

            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();

            // Format Currency
            const formatter = new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR',
                maximumFractionDigits: 0
            });

            // Populate Output UI Cards
            // Agent 1
            document.getElementById('out-health-score').textContent = data.health_score;
            document.getElementById('out-condition').textContent = data.condition;
            
            // Agent 2
            document.getElementById('out-risk-score').textContent = data.risk_score;
            document.getElementById('out-risk-level').textContent = data.risk_level;
            
            // Agent 3
            const priorityEl = document.getElementById('out-priority');
            priorityEl.textContent = data.priority;
            
            let colorClasses = 'bg-slate-200 text-slate-700 border-slate-300';
            if (data.priority === 'critical') colorClasses = 'bg-red-100 text-red-700 border-red-300';
            else if (data.priority === 'high') colorClasses = 'bg-orange-100 text-orange-700 border-orange-300';
            else if (data.priority === 'medium') colorClasses = 'bg-blue-100 text-blue-700 border-blue-300';
            
            priorityEl.className = `inline-block px-4 py-2 rounded-lg text-lg font-extrabold uppercase tracking-widest border ${colorClasses}`;
            
            // Agent 4
            document.getElementById('out-action').textContent = data.maintenance_action;
            
            // Agent 5
            document.getElementById('out-cost').textContent = formatter.format(data.cost);
            document.getElementById('out-workers').textContent = data.workers;
            document.getElementById('out-days').textContent = data.days + ' Days';
            
            // Agent 6
            document.getElementById('out-llm').textContent = data.recommendation;

            // Reveal Results
            loadingState.classList.add('hidden');
            resultsContainer.classList.remove('hidden');
            resultsContainer.classList.remove('opacity-50', 'pointer-events-none');

        } catch (error) {
            console.error('Error connecting to backend:', error);
            alert('Failed to connect to the backend. Please ensure Python server.py is running on port 8000.');
            loadingState.classList.add('hidden');
            resultsContainer.classList.remove('hidden');
        } finally {
            // Restore button
            analyzeBtn.innerHTML = originalBtnContent;
            analyzeBtn.disabled = false;
        }
    });
});
