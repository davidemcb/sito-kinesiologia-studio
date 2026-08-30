// CookieConsent configuration for kinesiologiastudio.it
window.CookieConsent = window.CookieConsent || {};

// Initialize CookieConsent library
(function() {
  const script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@3.0.1/cookieconsent.umd.js';
  script.onload = function() {
    // Configure CookieConsent
    CookieConsent.run({
      onFirstConsent: loadGoogleTag,
      onConsent: loadGoogleTag,
      onChange: loadGoogleTag,
      categories: {
        necessary: {
          services: {
            cloudflare: {}
          }
        },
        marketing: {}
      },
      language: {
        default: 'it',
        translations: {
          it: {
            consentModal: {
              title: 'Gestione dei cookie',
              description: 'Utilizziamo cookie essenziali e di marketing per offrirti la migliore esperienza. Puoi accettare o rifiutare i cookie di marketing.',
              acceptAllBtn: 'Accetta tutto',
              acceptNecessaryBtn: 'Solo essenziali',
              showPreferencesBtn: 'Gestisci preferenze'
            },
            preferencesModal: {
              title: 'Preferenze cookie',
              acceptAllBtn: 'Accetta tutto',
              acceptNecessaryBtn: 'Solo essenziali',
              savePreferencesBtn: 'Salva preferenze',
              sections: [
                {
                  title: 'Cookie essenziali',
                  description: 'Necessari al funzionamento del sito',
                  linkedCategory: 'necessary'
                },
                {
                  title: 'Cookie di marketing',
                  description: 'Utilizzati per analizzare le tue azioni e migliorare il sito',
                  linkedCategory: 'marketing'
                }
              ]
            }
          }
        }
      }
    });
  };
  document.head.appendChild(script);

  // Load Google tag when marketing consent is given
  window.loadGoogleTag = function() {
    const consentLevel = CookieConsent.getCategories();
    if (consentLevel && consentLevel.marketing) {
      // Only load gtag if not already loaded
      if (!window.gtag) {
        const gtag_script = document.createElement('script');
        gtag_script.async = true;
        gtag_script.src = 'https://www.googletagmanager.com/gtag/js?id=AW-969285863';
        document.head.appendChild(gtag_script);

        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        window.gtag = gtag;
        gtag('js', new Date());
        gtag('config', 'AW-969285863', {
          'anonymize_ip': true
        });
      }
    }
  };
})();
