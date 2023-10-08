

    htmx.on('htmx:beforeRequest', (evt) => {
        if (evt.detail.elt.id === 'form') {
            htmx.find('#start-upload').style.display = 'none';
            htmx.find('#loader').style.display = 'block';
            htmx.find('#upload-path').style.visibility = 'hidden';
            htmx.find('#percent-wrapper').style.visibility = 'visible';
        }
    });

    htmx.on('htmx:configRequest', (evt) => {
        if (evt.detail.elt.id === 'form') {
            event.detail.headers = []; // We clear the headers due to a bug in htmx: https://github.com/bigskysoftware/htmx/issues/779#issuecomment-1019373147
        }
    });

    htmx.on('htmx:afterOnLoad', (evt) => {
        if (evt.detail.elt.id === 'form') {
            htmx.find('#loader').style.display = 'none';
            htmx.find('#upload-path').style.visibility = 'visible';
            htmx.find('#start-upload').style.display = 'block';
        }
    });