// Conversion tracking for Kinesiologia Studio
// Tracks "Chiama" (call) and "Prenota" (booking) conversions

const conversionLabels = {
  'chiama': 'AW-969285863/HL7pCIvAp-scEOfBmM4D',
  'prenota': 'AW-969285863/zQe9CKf8nOscEOfBmM4D'
};

/**
 * Track a conversion event
 * @param {string} type - Type of conversion: 'chiama' or 'prenota'
 */
function trackConversion(type) {
  if (!window.gtag) {
    console.warn('Google tag not loaded yet. Conversion will not be tracked.');
    return true; // Allow link/action to proceed even if gtag not loaded
  }

  const label = conversionLabels[type];
  if (!label) {
    console.error('Unknown conversion type:', type);
    return true;
  }

  gtag('event', 'conversion', {
    'send_to': label,
    'value': type === 'prenota' ? 90.0 : 1.0,
    'currency': 'EUR'
  });

  console.log('Conversion tracked:', type, label);
  return true; // Allow links to proceed
}

/**
 * Setup Calendly conversion tracking
 * Listens for Calendly event scheduled messages
 */
function setupCalendlyConversion() {
  if (window.Calendly) {
    window.Calendly.initInlineWidget({
      url: 'https://calendly.com/scuderidavide/prima-valutazione',
      parentElement: document.getElementById('calendly-inline-widget')
    });

    // Listen for Calendly events
    window.addEventListener('message', function(event) {
      if (event.data.event && event.data.event.indexOf('calendly') === 0) {
        if (event.data.event === 'calendly.event_scheduled') {
          trackConversion('prenota');
        }
      }
    });
  }
}

// Initialize Calendly conversion tracking when page loads
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', setupCalendlyConversion);
} else {
  setupCalendlyConversion();
}
