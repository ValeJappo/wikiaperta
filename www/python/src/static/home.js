// Create Main page
function HomePage( name, config ) {
    HomePage.super.call( this, name, config );
    var contacts_msg=new OO.ui.ButtonWidget( {
        icon: 'userTalk',
        label: "Contatti",
        href: "#contacts"
    } );
    var documentazione=new OO.ui.ButtonWidget( {
        label: 'Documentazione',
        icon: 'book',
        href: "#docs"
    } );
    var codice=new OO.ui.ButtonWidget( {
        label: 'Codice',
        icon: 'code',
        href: '#code'
    } );
    this.$element.append( '<p>Pagina principale.</p>' );
    this.$element.append(documentazione.$element, contacts_msg.$element, codice.$element);
}
OO.inheritClass( HomePage, OO.ui.PageLayout );
HomePage.prototype.setupOutlineItem = function () {
    this.outlineItem.setLabel( 'Pagina principale' );
};