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

// La prenotazione avviene sulla pagina appuntamenti di Google Calendar,
// che si apre in una nuova scheda: la conversione viene tracciata al clic
// sul pulsante tramite onclick="trackConversion('prenota')".
